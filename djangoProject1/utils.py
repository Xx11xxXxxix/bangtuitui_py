import json
import random

from django.conf import settings
from django.http import QueryDict


def get_request_data(request):
    """
    封装提取 request 数据的逻辑，根据请求方法和请求体类型自动解析数据
    """
    if request.method == 'GET':
        return request.GET.dict()

    elif request.method in ['POST', 'PUT', 'PATCH']:
        content_type = request.content_type

        if content_type == 'application/json':
            # 解析 JSON 数据
            try:
                body_unicode = request.body.decode('utf-8')
                body_data = json.loads(body_unicode)
                return body_data
            except (json.JSONDecodeError, UnicodeDecodeError) as e:
                print(f"error:{e}")
                return {'error': 'Invalid JSON format'}
        elif content_type == 'application/x-www-form-urlencoded' or content_type == 'multipart/form-data':
            # 解析表单数据
            return request.POST.dict()

    def get_version():
        return "1.0.0"

    return {}



def get_version():
    return "1.0.0"
