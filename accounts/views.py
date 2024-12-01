from django.core.cache import cache
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.hashers import make_password
from common.views import generate_code
from accounts.models import AccountsUser


def send_sms_code(request):
    data = json.loads(request.body)
    phone_number = data.get('phone_number')
    code = generate_code(phone_number)
    print(code)
    return JsonResponse({
        'code': code,
        'msg': 'code-DONE!'
    })


@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        phone_number = data.get('phone_number')
        username = data.get('username')
        password = data.get('password')
        captcha_response = data.get('captcha')  # 用户提交的验证码
        code = data.get('code')
        cache_key = f'sms_code_{phone_number}'
        cached_code = cache.get(cache_key)
        if code != cached_code:
            return JsonResponse({'code': '0', 'msg': 'CODE-WRONG'})
        # 检查必要字段
        # if not phone_number or not password or not captcha_response:
        #     return JsonResponse({'status': 'fail', 'message': '缺少手机号、密码或验证码'}, status=400)
        # print(captcha_response)
        # # 验证验证码
        # if not CaptchaStore.objects.filter(response=captcha_response).exists():
        #     return JsonResponse({'status': 'fail', 'message': 'yanzhengmacuo'}, status=400)

        # 检查用户是否已存在
        try:
            user = AccountsUser.objects.get(phone_number=phone_number)
            return JsonResponse({'status': 'fail', 'message': '用户已存在'}, status=400)
        except AccountsUser.DoesNotExist:
            pass  # 用户不存在

        # # 检查是否已经注册
        # if AccountsUser.objects.filter(phone_number=phone_number).exists():
        #     return JsonResponse({'status': 'fail', 'message': '手机号已注册'}, status=400)

        # 创建用户并保存到数据库
        hashed_password = make_password(password)
        new_user = AccountsUser.objects.create(
            username=username,
            phone_number=phone_number,
            password=hashed_password
        )

        return JsonResponse({'status': 'success', 'message': '注册成功', 'uid': new_user.uid})
    return JsonResponse({'status': 'fail', 'message': '仅支持POST请求'}, status=400)
