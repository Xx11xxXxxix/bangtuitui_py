from typing import List
from django.db import models
from django.conf import settings

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
    create_time = models.IntegerField(default=0, verbose_name='创建时间')
    update_time = models.IntegerField(default=0, verbose_name='更新时间')

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

    @classmethod
    def get_list(cls):
        all_menus=cls.new_get_all(is_show=1)

        return cls.recursive_menu_array(all_menus,parent_id=0)

    @classmethod
    def new_get_all(cls,is_show=1):
        """所有记录"""
        if is_show==1:
            queryset=cls.objects.filter(is_show=is_show)
        else:
            queryset=cls.objects.all()
        return list(queryset.order_by('sort', 'create_time').values())

    @classmethod
    def get_list_by_user(cls,shop_user_id):
        """用户权限菜单"""
        #用户角色
        all_roles = UserRole.objects.all()
        role_ids=UserRole.objects.filter(
            shop_user_id=shop_user_id,
        ).values_list('role_id',flat=True)

        #角色权限
        access_ids=RoleAccess.objects.filter(
            role_id__in=role_ids,
        ).values_list('access_id',flat=True)

        #权限菜单
        menus_list=cls.objects.filter(
            access_id__in=access_ids
        ).order_by('sort', 'create_time')


        ##格式树形结构
        return cls.newformat_tree_data(menus_list,parent_id=0)

    @staticmethod
    def recursive_menu_array(items,parent_id=0):
        """递归构建菜单树"""
        result=[]
        for item in items:
            if item['parent_id']==parent_id:
                children=Access.recursive_menu_array(items,item['access_id'])
                if children:
                    item['children']=children
                result.append(item)
        return result

    @staticmethod
    def newformat_tree_data(queryset, parent_id=0):
        """格式化树形结构
        Args:
            queryset: Access查询集
            parent_id: 父级ID
        Returns:
            list: 树形结构的菜单列表
        """
        result = []
        items = list(queryset.values())
        for item in items:
            if item['parent_id'] == parent_id:
                children = Access.recursive_menu_array(items, item['access_id'])
                if children:
                    item['children'] = children
                result.append(item)

        return result

###bangtuitui_py_shop_role表
class Role(models.Model):
    """角色模型"""
    role_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name='角色名称')
    description = models.TextField(blank=True, verbose_name='角色描述')
    created_at = models.IntegerField(default=0)

    class Meta:
        db_table = 'bangtuitui_py_shop_role'
        verbose_name = '角色'
        app_label = 'permissions'

###bangtuitui_py_shop_user_role表
class UserRole(models.Model):
    """用户-角色关联"""
    id = models.AutoField(primary_key=True)
    shop_user_id = models.IntegerField()
    role_id = models.IntegerField()
    create_time = models.IntegerField(default=0)

    class Meta:
        db_table = 'bangtuitui_py_shop_user_role'
        verbose_name = '用户角色关联'
        app_label = 'permissions'

    @classmethod
    def get_role_ids(cls, shop_user_id):
        return cls.objects.filter(
            shop_user_id=shop_user_id
        ).values_list('role_id', flat=True)

###bangtuitui_py_shop_role_access表
class RoleAccess(models.Model):
    """角色-权限关联"""
    id = models.AutoField(primary_key=True)
    role_id = models.IntegerField()
    access_id = models.IntegerField()
    created_at = models.IntegerField(default=0)

    class Meta:
        db_table = 'bangtuitui_py_shop_role_access'
        verbose_name = '角色权限关联'
        app_label = 'permissions'

    @classmethod
    def get_access_ids(cls, role_ids):
        return cls.objects.filter(
            role_id__in=role_ids
        ).values_list('access_id', flat=True)