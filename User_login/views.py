from django.core.cache import cache
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import check_password
from accounts.models import AccountsUser  # 导入 AccountsUser 模型
from captcha.models import CaptchaStore
import json

from common.views import BaseController


@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        try:
            # 获取请求体中的数据
            data = json.loads(request.body)
            phone_number = data.get('phone_number')
            password = data.get('password')
            captcha_response = data.get('captcha')  # 用户提交的验证码
            code = data.get('code')
            cache_key = f'sms_code_{phone_number}'
            cached_code = cache.get(cache_key)
            if code != cached_code:
                return JsonResponse({'code': '0', 'msg': 'CODE-WRONG'})
            # 检查必要的字段是否存在
            # if not phone_number or not password:
            #     return JsonResponse({'status': 'fail', 'message': '缺少手机号或密码'}, status=400)
            #
            # # 验证验证码
            # if not CaptchaStore.objects.filter(response=captcha_response).exists():
            #     return JsonResponse({'status': 'fail', 'message': 'meiyanzhengma'}, status=400)

            # 检查用户是否存在
            try:
                user = AccountsUser.objects.get(phone_number=phone_number)
                print(f"User found: {user}")
            except AccountsUser.DoesNotExist:
                print(f"User with phone number {phone_number} 这个表.")
                return JsonResponse({'status': 'fail', 'msg': '用户不存在'}, status=400)

            # 验证密码是否正确
            if not check_password(password, user.password):
                return JsonResponse({'status': 'fail', 'msg': '密码错误'}, status=400)

            # 创建并保存用户的 token
            user.token = BaseController.sign_token(user.uid)
            #
            # return JsonResponse({
            #     'code':1,
            #     'status': 'success',
            #     'msg': '登录成功',
            #     'token': user.token,
            #     'uid': user.uid,
            #     'username': user.username
            # })
            #todo 应该是几把要改返回内容忘了都要啥了
            return JsonResponse({
                'code': 1,
                'msg': '登录成功',
                'data': {
                    # 'app_id': user_info.app_id,
                    # 'user_name': user_info.user_name,
                    # 'token': user_info.token,
                    # 'version': version,
                    # 'platform_code': user_info.platform_code,
                    # 'is_super': user_info.is_super
                    'token': user.token,
                    'uid': user.uid,
                    'username': user.username
                }
            })

        except json.JSONDecodeError:
            return JsonResponse({'status': 'fail', 'msg': '请求体不是有效的JSON'}, status=400)

        except Exception as e:
            # 捕获所有其他异常并返回信息
            return JsonResponse({'status': 'fail', 'msg': '服务器错误', 'error': str(e)}, status=500)

    return JsonResponse({'status': 'fail', 'msg': '仅支持POST请求'}, status=400)
