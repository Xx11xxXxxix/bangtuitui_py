# services/auth_service.py

from django.core.cache import cache
from typing import List
import re
from models.Role.RoleAccess import RoleAccess
from models.User.UserRole import UserRole
from models.authRole.Auth import Access


class AuthService:
    # 存放实例
    _instance = None

    # 商家登录信息
    def __init__(self, store):
        # 初始化商家信息和当前用户信息
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
        """获取 AuthService 的单例实例"""
        if cls._instance is None:
            cls._instance = cls(store)
        return cls._instance

    def check_privilege(self, url: str or List[str], strict=True) -> bool:
        """验证指定 URL 是否有访问权限"""
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
        """检查单个 URL 是否有权限访问"""
        # 超级管理员无需验证
        if self.user.is_super:
            return True
        # 检查是否在白名单中
        if url in self.allow_all_action or self.match_wildcard(url):
            return True
        # 检查用户权限
        return url in self.get_access_urls()

    def match_wildcard(self, url: str) -> bool:
        """通配符支持"""
        for action in self.allow_all_action:
            if '*' in action and self.wildcard_match(action, url):
                return True
        return False

    def wildcard_match(self, pattern: str, string: str) -> bool:
        """实现简单的通配符匹配"""
        pattern = pattern.replace('*', '.*')
        return bool(re.match(pattern, string))

    def get_access_urls(self) -> List[str]:
        """获取当前用户的权限 URL 列表"""
        if not self.access_urls:
            # 获取用户的角色 ID 集合
            role_ids = UserRole.objects.filter(shop_user_id=self.user.id).values_list('role_id', flat=True)
            # 根据角色 ID 获取权限 ID 集合
            access_ids = RoleAccess.objects.filter(role_id__in=role_ids).values_list('access_id', flat=True)
            # 根据权限 ID 获取权限 URL
            self.access_urls = list(Access.get_access_urls(access_ids))
        return self.access_urls

    @staticmethod
    def get_access_name_by_path(path: str, app_id: int) -> str:
        """根据路径和 app_id 获取权限名称"""
        cache_key = f'path_access_{app_id}'
        access_cache = cache.get(cache_key)

        if not access_cache:
            # 缓存中不存在时查询数据库
            access_list = Access.objects.values('name', 'path')
            access_cache = {item['path']: item['name'] for item in access_list}
            cache.set(cache_key, access_cache, timeout=3600)

        return access_cache.get(path, '')

