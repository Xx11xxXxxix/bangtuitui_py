from django.shortcuts import render
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from common.views import BaseController
from .models import User
from djangoProject1.utils import get_version
import json
import time

@method_decorator(csrf_exempt, name='dispatch')
class PassportView(View):
    def post(self,request):
        try:
            user_data = json.loads(request.body)
            user_info = User.check_login(user_data)

            if user_info:
                version = get_version()

                return JsonResponse({
                    'code': 1,
                    'message': '登录成功',
                    'data': {
                        'app_id': user_info.app_id,
                        'user_name': user_info.user_name,
                        'token': user_info.token,
                        'version': version,
                        'platform_code': user_info.platform_code,
                        'is_super': user_info.is_super
                    }
                })
            else:
                return JsonResponse({
                    'code': 0,
                    'msg': User.get_error()
                })
        except Exception as e:
            print(f"登录是啊比: {str(e)}")
            return JsonResponse({
                'code': 0,
                'msg': f'接口有错: {str(e)}'
            })




