from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token
from accounts.models import AccountsUser  # 导入 AccountsUser 模型
import json

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        try:
            # 检查请求体是否为空
            if not request.body:
                return JsonResponse({'status': 'fail', 'message': '请求体为空'}, status=400)

            # 获取请求体中的数据
            data = json.loads(request.body)
            phone_number = data.get('phone_number')
            password = data.get('password')

            # 检查必要的字段是否存在
            if not phone_number or not password:
                return JsonResponse({'status': 'fail', 'message': '缺少手机号或密码'}, status=400)

            # 检查用户是否存在
            try:
                user = AccountsUser.objects.get(phone_number=phone_number)
                print(f"User with phone number {phone_number} does not exist.")

            except AccountsUser.DoesNotExist:
                print(f"User with phone number {phone_number} does not exist.")
                return JsonResponse({'status': 'fail', 'message': '用户不存在'}, status=400)

            # 验证密码是否正确
            if not check_password(password, user.password):
                return JsonResponse({'status': 'fail', 'message': '密码错误'}, status=400)

            # 获取或创建 Token
            token, created = Token.objects.get_or_create(user=user)

            return JsonResponse({
                'status': 'success',
                'message': '登录成功',
                'token': token.key,
                'uid': user.uid,
                'username': user.username
            })

        except json.JSONDecodeError:
            return JsonResponse({'status': 'fail', 'message': '请求体不是有效的JSON'}, status=400)

        except Exception as e:
            # 捕获所有其他异常并返回信息
            return JsonResponse({'status': 'fail', 'message': '服务器错误', 'error': str(e)}, status=500)

    return JsonResponse({'status': 'fail', 'message': '仅支持POST请求'}, status=400)