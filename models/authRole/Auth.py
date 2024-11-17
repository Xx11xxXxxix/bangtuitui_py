from typing import List
from django.db import models

class Access(models.Model):
    access_id = models.AutoField(primary_key=True, db_column='access_id')
    name = models.CharField(max_length=255, default='', verbose_name='权限名称')
    path = models.CharField(max_length=128, default='', blank=True, verbose_name='路由地址')
    parent_id = models.IntegerField(default=0, verbose_name='父级id')
    sort = models.PositiveSmallIntegerField(default=100, verbose_name='排序')
    icon = models.CharField(max_length=128, blank=True, verbose_name='菜单图标')
    redirect_name = models.CharField(max_length=128, blank=True, verbose_name='重定向名称')
    is_route = models.BooleanField(default=False, verbose_name='是否是路由')
    is_menu = models.BooleanField(default=False, verbose_name='是否是菜单')
    alias = models.CharField(max_length=128, blank=True, verbose_name='别名')
    is_show = models.BooleanField(default=True, verbose_name='是否显示')
    plus_category_id = models.IntegerField(default=0, blank=True, verbose_name='插件分类id')
    remark = models.CharField(max_length=255, blank=True, verbose_name='描述')
    app_id = models.PositiveIntegerField(default=10001, blank=True, verbose_name='app_id')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        db_table = 'bangtuitui_py_shop_access'
        verbose_name = '商家用户权限'
        ordering = ['sort', 'create_time']
        app_label = 'Auth'

    def __str__(self):
        return self.name

    @staticmethod
    def get_all(is_show=1):
        """获取所有权限"""
        queryset = Access.objects.all()
        if is_show != -1:
            queryset = queryset.filter(is_show=is_show)
        return queryset.order_by('sort', 'create_time')

    @staticmethod
    def detail(access_id=None, **kwargs):
        """获取单个权限详情"""
        if access_id:
            return Access.objects.filter(access_id=access_id).first()
        return Access.objects.filter(**kwargs).first()

    @staticmethod
    def get_access_urls(access_ids: List[int]):
        """根据权限ID获取权限URL列表"""
        return Access.objects.filter(access_id__in=access_ids, is_show=True).values_list('path', flat=True)

    @staticmethod
    def get_access_list(access_ids: List[int]):
        """获取指定权限ID的权限列表"""
        return Access.objects.filter(access_id__in=access_ids).order_by('sort', 'create_time')

    @staticmethod
    def get_list_by_plus_category_id(category_id: int):
        """根据插件分类ID查询权限"""
        return Access.objects.filter(plus_category_id=category_id, is_show=True).order_by('sort', 'create_time')

    def format_tree_data(self, parent_id=0):
        """递归生成权限树"""
        tree = []
        nodes = Access.objects.filter(parent_id=parent_id)
        for node in nodes:
            item = {
                'access_id': node.access_id,
                'name': node.name,
                'path': node.path,
                'children': self.format_tree_data(node.access_id)
            }
            tree.append(item)
        return tree
