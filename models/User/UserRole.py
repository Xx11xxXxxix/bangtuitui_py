from django.db import models

class UserRole(models.Model):
    shop_user_id = models.IntegerField(db_index=True, verbose_name="超管用户ID")
    role_id = models.IntegerField(verbose_name="角色ID")
    app_id = models.IntegerField(default=0, verbose_name="小程序ID")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, null=True, verbose_name="更新时间")

    class Meta:
        app_label = 'UserRole'
        db_table = 'bangtuitui_py_shop_user_role'
        verbose_name = "商家用户角色记录"
        verbose_name_plural = "商家用户角色记录"
        indexes = [
            models.Index(fields=['shop_user_id'], name='admin_user_id')
        ]

    def __str__(self):
        return f"UserRole(shop_user_id={self.shop_user_id}, role_id={self.role_id})"
