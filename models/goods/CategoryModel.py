# models.py

from django.core.cache import cache
from django.db import models

from models.goods.GoodsModel import Product


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name="分类名称")
    parent_id = models.IntegerField(default=0, verbose_name="父级分类ID")
    sort = models.IntegerField(default=0, verbose_name="排序")
    image_id = models.IntegerField(null=True, blank=True, verbose_name="图片ID")
    app_id = models.IntegerField(default=10001, verbose_name="应用ID")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        db_table = 'bangtuitui_py_category'
        ordering = ['sort', 'create_time']
        verbose_name = "商品分类"
        verbose_name_plural = "商品分类"
        app_label = 'goods'

    def __str__(self):
        return self.name

    def add(self, data):
        """添加新记录"""
        data['app_id'] = self.app_id
        self.delete_cache()
        return Category.objects.create(**data)

    def edit(self, data):
        """编辑记录"""
        # 验证是否可以移动分类
        if data['parent_id'] > 0 and Category.has_sub_category(self.category_id):
            raise ValueError('该分类下存在子分类，不可以移动')

        self.delete_cache()
        data['image_id'] = data.get('image_id', 0)
        for field, value in data.items():
            setattr(self, field, value)
        self.save()
        return True

    def remove(self):
        """删除商品分类"""
        if Product.objects.filter(category_id=self.category_id).exists():
            raise ValueError(f'该分类下存在商品，不允许删除')
        if Category.has_sub_category(self.category_id):
            raise ValueError('该分类下存在子分类，请先删除')

        self.delete_cache()
        self.delete()
        return True

    @staticmethod
    def delete_cache():
        """删除缓存"""
        cache.delete('category_cache')

    @staticmethod
    def get_all():
        """获取所有分类，带缓存"""
        cache_key = 'category_cache'
        cached_data = cache.get(cache_key)

        if not cached_data:
            all_categories = Category.objects.all().order_by('sort', 'create_time')
            # all_categories = Category.objects.all().select_related('image').order_by('sort', 'create_time')
            tree = Category.build_tree(all_categories)
            cache.set(cache_key, {'all': list(all_categories), 'tree': tree}, timeout=3600)
            return {'all': list(all_categories), 'tree': tree}

        return cached_data

    @staticmethod
    def build_tree(categories):
        """生成树状结构的分类"""
        all_categories = list(categories)
        tree = []
        for first in all_categories:
            if first.parent_id != 0:
                continue
            two_tree = []
            for second in all_categories:
                if second.parent_id != first.category_id:
                    continue
                three_tree = [third for third in all_categories if third.parent_id == second.category_id]
                if three_tree:
                    second.child = three_tree
                two_tree.append(second)
            if two_tree:
                first.child = sorted(two_tree, key=lambda x: x.sort)
            tree.append(first)
        return tree

    @staticmethod
    def get_cache_all():
        """获取所有分类"""
        return Category.get_all().get('all', [])

    @staticmethod
    def get_cache_tree():
        """获取分类树状结构"""
        tree = Category.get_all().get('tree', [])
        return [category.to_dict() for category in tree]

    @staticmethod
    def get_cache_tree_json():
        """获取树状结构的分类并转换为 JSON 格式"""
        import json
        return json.dumps(Category.get_cache_tree())

    def to_dict(self):
        """将 Category 对象转换为字典格式"""
        return {
            'category_id': self.category_id,
            'name': self.name,
            'parent_id': self.parent_id,
            'sort': self.sort,
            'image_id': self.image_id,
            'app_id': self.app_id,
            'create_time': self.create_time,
            'update_time': self.update_time,
        }

    @staticmethod
    def get_sub_category_ids(parent_id, all_categories=None):
        """获取指定分类下的所有子分类ID"""
        if all_categories is None:
            all_categories = Category.get_cache_all()
        ids = [parent_id]
        for category in all_categories:
            if category.parent_id == parent_id:
                ids.extend(Category.get_sub_category_ids(category.category_id, all_categories))
        return ids

    @staticmethod
    def has_sub_category(parent_id):
        """判断指定分类下是否存在子分类"""
        return any(category.parent_id == parent_id for category in Category.get_cache_all())

    def get_list_by_ids(self, ids):
        """获取指定ID集合的分类列表"""
        return Category.objects.filter(category_id__in=ids).values('category_id', 'name', 'parent_id')

    # 关联到图片（先缺少图片模型 `UploadFile`）
    # def image(self):
    #     return self.belongs_to('app.common.model.file.UploadFile', 'image_id', 'file_id')
