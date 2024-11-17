# models.py

from django.db import models
from models.authRole.Auth import Access

class RoleAccess(models.Model):
    role_id = models.IntegerField(db_index=True, verbose_name="角色ID")
    access_id = models.ForeignKey(Access, on_delete=models.CASCADE, db_column='access_id', verbose_name="权限ID")
    app_id = models.IntegerField(default=0, verbose_name="小程序ID")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        app_label = 'RoleAccess'
        db_table = 'bangtuitui_py_shop_role_access'
        verbose_name = "商家用户角色权限关系"
        verbose_name_plural = "商家用户角色权限关系"
        indexes = [
            models.Index(fields=['role_id'], name='role_id_idx')
        ]

    def __str__(self):
        return f"RoleAccess(role_id={self.role_id}, access_id={self.access_id})"

    @staticmethod
    def get_access_ids(role_id):
        """
        获取指定角色的所有权限ID
        :param role_id: 角色ID，支持单个ID或ID列表
        :return: 包含权限ID的列表
        """
        role_ids = role_id if isinstance(role_id, list) else [role_id]
        access_ids = RoleAccess.objects.filter(role_id__in=role_ids).values_list('access_id', flat=True)
        return list(access_ids)
