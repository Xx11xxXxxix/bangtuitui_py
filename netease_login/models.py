# models.py
from django.db import models


class EaseapiLog(models.Model):
    api_name = models.CharField(max_length=100)
    request_params = models.TextField()
    response_data = models.JSONField()
    time = models.DateTimeField(auto_now_add=True)
    status_code = models.IntegerField()
    error_message = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'bangtuitui_py_easeapi_log'

    @classmethod
    def api_log(cls, api_name, request_params, response_data, status_code, error_message=None):
        try:
            cls.objects.create(
                api_name=api_name,
                request_params=request_params,
                response_data=response_data,
                status_code=status_code,
                error_message=error_message
            )
        except Exception as e:
            print(f"记录api日志错误: {str(e)}")

    @classmethod
    async def async_api_log(cls, api_name, request_params, response_data, status_code, error_message=None):
        from asgiref.sync import sync_to_async
        try:
            await sync_to_async(cls.api_log)(
                api_name=api_name,
                request_params=request_params,
                response_data=response_data,
                status_code=status_code,
                error_message=error_message
            )
        except Exception as e:
            print(f"异步记录日志失败: {str(e)}")


class EaseapiUser(models.Model):
    user_id = models.BigIntegerField(unique=True)
    nickname = models.CharField(max_length=100, null=True, blank=True)
    music_u = models.TextField()
    avatar_url = models.CharField(max_length=255, null=True, blank=True)
    background_url = models.CharField(max_length=255, null=True, blank=True)
    signature = models.TextField(null=True, blank=True)
    birthday = models.BigIntegerField(null=True, blank=True)
    gender = models.SmallIntegerField(null=True, blank=True)
    province = models.IntegerField(null=True, blank=True)
    city = models.IntegerField(null=True, blank=True)
    vip_type = models.SmallIntegerField(null=True, blank=True)
    account_type = models.SmallIntegerField(null=True, blank=True)
    authority = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    detail_description = models.TextField(null=True, blank=True)
    auth_status = models.SmallIntegerField(null=True, blank=True)
    last_login_time = models.BigIntegerField(null=True, blank=True)
    last_login_ip = models.CharField(max_length=50, null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'bangtuitui_py_easeapi_user'

    @classmethod
    def update_user(cls, profile, music_u):
        try:
            user, created = cls.objects.update_or_create(
                user_id=profile.get('userId'),
                defaults={
                    'nickname': profile.get('nickname'),
                    'music_u': music_u,
                    'avatar_url': profile.get('avatarUrl'),
                    'background_url': profile.get('backgroundUrl'),
                    'signature': profile.get('signature'),
                    'birthday': profile.get('birthday'),
                    'gender': profile.get('gender'),
                    'province': profile.get('province'),
                    'city': profile.get('city'),
                    'vip_type': profile.get('vipType'),
                    'account_type': profile.get('accountType'),
                    'authority': profile.get('authority'),
                    'description': profile.get('description'),
                    'detail_description': profile.get('detailDescription'),
                    'auth_status': profile.get('authStatus'),
                    'last_login_time': profile.get('lastLoginTime'),
                    'last_login_ip': profile.get('lastLoginIP'),
                }
            )
            return user, created
        except Exception as e:
            print(f"更新用户信息失败: {str(e)}")
            raise e