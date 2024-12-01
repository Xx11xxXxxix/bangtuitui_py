from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.hashers import make_password
from accounts.models import AccountsUser


@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        phone_number = data.get('phone_number')
        username = data.get('username')
        password = data.get('password')


        # 检查是否已经注册
        if AccountsUser.objects.filter(phone_number=phone_number).exists():
            return JsonResponse({'status': 'fail', 'message': '手机号已注册'}, status=400)

        # 创建用户并保存到数据库
        hashed_password = make_password(password)
        new_user = AccountsUser.objects.create(
            username=username,
            phone_number=phone_number,
            password=hashed_password
        )

        return JsonResponse({'status': 'success', 'message': '注册成功', 'uid': new_user.uid})
    return JsonResponse({'status': 'fail', 'message': '仅支持POST请求'}, status=400)