from urllib import request

from django.db import models
from django.utils import timezone
import time

from common.views import BaseController


class User(models.Model):
    shop_user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=255, default='')
    password = models.CharField(max_length=255, default='')
    real_name = models.CharField(max_length=255, default='')
    is_super = models.IntegerField(default=0)
    is_delete = models.IntegerField(default=0)
    app_id = models.IntegerField(default=0)
    create_time = models.IntegerField(default=0)
    update_time = models.IntegerField()
    user_id = models.IntegerField(null=True, blank=True)
    platform_code = models.CharField(max_length=50, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    _token = None


    class Meta:
        db_table = 'bangtuitui_py_shop_user'
        managed = False##数据库迁移不用这个表
    @classmethod
    def check_login(cls, user_data):
        try:
            user = cls.objects.get(
                user_name=user_data.get('username'),
                is_delete=0
            )

            # 创建并保存用户的 token
            user.token = BaseController.sign_token(user.shop_user_id)
            user.save()
            request.user = user
            return user

        except cls.DoesNotExist:
            cls.error = '用户名或密码错误'
            return False

        except Exception as e:
            print(f"{e}:")

            cls.error = f's登录失败: {str(e)}'
            return False

    @classmethod
    def get_error(cls):
        return cls.error if hasattr(cls, '请求失败') else None



class SettingModel(models.Model):
    name = models.CharField(max_length=255, unique=True)
    value = models.TextField()
    is_delete = models.BooleanField(default=False)

    @staticmethod
    def get_item(name):
        try:
            setting = SettingModel.objects.get(name=name, is_delete=False)
            return {'name': setting.value}
        except SettingModel.DoesNotExist:
            return {'name': 'Default Shop'}