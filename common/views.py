import time

import jwt
from django.http import JsonResponse
from django.views import View
from django.conf import settings
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.core.cache import cache
# from shop.services.auth_service import AuthService
import logging

from jwt.exceptions import InvalidSignatureError, ExpiredSignatureError, InvalidTokenError

from models.User.UserRole import UserRole
from services.Authservice import AuthService

logger = logging.getLogger(__name__)


class BaseController(View):
    store = {}
    allow_all_actions = ['/passport/login', '/index/base']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.route_uri = None
        self.action = None
        self.controller = None

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.get_route_info(request)
        if not self.check_login(request):
            return JsonResponse({'msg': '没登录！', 'code': -1})
        self.save_opt_log(request)
        if not self.check_privilege():
            return JsonResponse({'msg': '没有访问权限', 'code': -1})
        return super().dispatch(request, *args, **kwargs)

    def get_route_info(self, request):
        self.controller = request.resolver_match.view_name
        self.action = request.method.lower()
        self.route_uri = request.path

    def check_login(self, request):
        # 检查请求是否在白名单
        if self.route_uri in self.allow_all_actions:
            return True
        token = request.headers.get('Token') or request.GET.get('token')
        if not token:
            print('not token')

            return False
        data = self.check_token(token)
        if data.get('code') != 1:

            return False
        user_data = data.get('data')
        # if user_data.get('type') != 'shop':
        #     return False
        from admin.denglu.models import User
        print(user_data.get('user_id'))

        user = User.objects.filter(shop_user_id=user_data.get('user_id')).first()
        request.user = user
        if not user:
            print('没有此用户')

            return False
        roles = UserRole.objects.filter(shop_user_id=user.shop_user_id).values_list('role_id', flat=True)
        self.store = {
            'user': {
                'shop_user_id': user.shop_user_id,
                'user_name': user.user_name,
                'user_role': list(roles),
                'is_super': user.is_super,
                'user_id': user.user_id
            },
            # 'app': user.app.to_dict()
        }
        return True

    def save_opt_log(self, request):
        if not self.store:
            return
        shop_user_id = self.store['user']['shop_user_id']
        if not shop_user_id:
            return
        config = getattr(settings, 'STORE_CONFIG', {})
        if not config.get('is_get_log'):
            return
        # OptLog.objects.create(
        #     shop_user_id=shop_user_id,
        #     ip=request.META.get('REMOTE_ADDR'),
        #     request_type='Get' if request.method == 'GET' else 'Post',
        #     url=self.route_uri,
        #     content=json.dumps(request.GET if request.method == 'GET' else request.POST, ensure_ascii=False),
        #     browser=self.get_client_browser(request),
        #     agent=request.META.get('HTTP_USER_AGENT'),
        #     title=AuthService.get_access_name_by_path(self.route_uri, self.store['app']['app_id']),
        #     app_id=self.store['app']['app_id']
        # )

    def check_privilege(self):
        if not self.store:
            return False
        auth_service = AuthService(self.store)
        if not auth_service.check_privilege(self.route_uri):
            return False
        return True

    def get_user(self, is_force=True):
        token = self.request.GET.get('token')
        if not token and is_force:
            raise Exception('缺少必要的参数：token')
        user = self.get_user_by_token(token)
        if not user and is_force:
            raise Exception('没有找到用户信息')
        if user.is_deleted:
            cache.delete(token)
            raise Exception('没有找到用户信息')
        return user

    #创建token和识别token
    def sign_token(user_id):
        payload = {
            "user_id": user_id,
            "timestamp": int(time.time())
        }
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
        return token

    @staticmethod
    def get_user_by_token(token):
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user_id = payload.get("user_id")
            from admin.denglu.models import User

            user = User.objects.filter(id=user_id).first()
            if user and not user.is_deleted:
                return user
        except (ExpiredSignatureError, InvalidTokenError):
            return None
        return None

    # 创建token和识别token

    def get_client_browser(self, request):
        # 简单的浏览器检测逻辑
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        if 'Chrome' in user_agent:
            return 'Chrome'
        elif 'Firefox' in user_agent:
            return 'Firefox'
        return 'Unknown'

    @staticmethod
    def check_token(token):
        key = f"{settings.SECRET_KEY}"  # 使用 SECRET_KEY 和 token_type

        try:
            decoded = jwt.decode(token, key, algorithms=["HS256"], options={"verify_exp": True, "leeway": 60})
            # print('打印的', decoded)
            return {"code": 1, "data": decoded}
        except InvalidSignatureError:
            # print('签名不正确')

            return {"code": -1, "msg": "签名不正确"}
        except ExpiredSignatureError:
            # print('token失效')

            return {"code": -1, "msg": "token失效"}
        except InvalidTokenError:
            # print('token无效  ')

            return {"code": -1, "msg": "token无效"}
        except Exception:
            # print('未知错误  ')

            return {"code": -1, "msg": "未知错误"}

