from typing import List
import re

from django.core.cache import cache

from permissions.models import Access, UserRole, RoleAccess


class PermissionService:
    def __init__(self, store):
        self.store = store
        self.user = store['user']

    def get_role_list(self):
        """权限列表"""
        if self.user.get('is_super'):
            menus = Access.get_list()
        else:
            menus = Access.get_list_by_user(self.user['shop_user_id'])
            print(menus)

            for menu in menus:
                if menu.get('redirect_name') != menu.get('children', [{}])[0].get('path'):
                    menu['redirect_name'] = menu.get('children', [{}])[0].get('path')
        return menus


class AuthService:
    """处理权限验证相关的业务逻辑"""
    _instance = None  # 单例实例

    def __init__(self, store):
        self.store = store
        from admin.denglu.models import User

        self.user = User.objects.filter(shop_user_id=self.store['user']['shop_user_id']).first()
        self.allow_all_action = [
            '/passport/login', '/passport/logout', '/index/index', '/passport/editPass',
            '/file/file/*', '/file/upload/image', '/data/*', '/product/spec/*',
            '/authRole/user/getUserInfo', '/authRole/user/getRoleList',
            '/statistics/sales/order', '/statistics/sales/product',
            '/statistics/user/scale', '/statistics/user/new_user', '/statistics/user/pay_user'
        ]
        self.access_urls = []

    @classmethod
    def get_instance(cls, store):
        """获取AuthService的单例实例"""
        if cls._instance is None:
            cls._instance = cls(store)
        return cls._instance

    def check_privilege(self, url: str or List[str], strict=True) -> bool:
        """验证指定URL是否有访问权限"""
        if isinstance(url, str):
            return self.check_access(url)
        else:
            for val in url:
                if strict and not self.check_access(val):
                    return False
                if not strict and self.check_access(val):
                    return True
        return True

    def check_access(self, url: str) -> bool:
        """检查单个URL是否有权限访问"""
        if self.user.is_super:
            return True
        if url in self.allow_all_action or self.match_wildcard(url):
            return True
        return url in self.get_access_urls()

    def match_wildcard(self, url: str) -> bool:
        """通配符匹配支持"""
        for action in self.allow_all_action:
            if '*' in action and self.wildcard_match(action, url):
                return True
        return False

    def wildcard_match(self, pattern: str, string: str) -> bool:
        """实现简单的通配符匹配"""
        pattern = pattern.replace('*', '.*')
        return bool(re.match(pattern, string))

    def get_access_urls(self) -> List[str]:
        """获取当前用户的权限URL列表"""
        if not self.access_urls:
            role_ids = UserRole.objects.filter(
                shop_user_id=self.user.id
            ).values_list('role_id', flat=True)

            access_ids = RoleAccess.objects.filter(
                role_id__in=role_ids
            ).values_list('access_id', flat=True)

            self.access_urls = list(Access.get_access_urls(access_ids))
        return self.access_urls

    @staticmethod
    def get_access_name_by_path(path: str, app_id: int) -> str:
        """根据路径和app_id获取权限名称"""
        cache_key = f'path_access_{app_id}'
        access_cache = cache.get(cache_key)

        if not access_cache:
            access_list = Access.objects.values('name', 'path')
            access_cache = {item['path']: item['name'] for item in access_list}
            cache.set(cache_key, access_cache, timeout=3600)

        return access_cache.get(path, '')