import time

from django.db import models
from django.utils import timezone
from django.core.cache import cache


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255, verbose_name="商品名称")
    product_status = models.IntegerField(default=10, choices=[(10, "上架"), (20, "下架"), (30, "草稿")], verbose_name="商品状态")
    product_stock = models.IntegerField(default=0, verbose_name="库存")
    product_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="价格")
    create_user_id = models.IntegerField(verbose_name="创建用户ID")
    grade_ids = models.CharField(max_length=255, blank=True, verbose_name="等级IDs")
    sales_initial = models.IntegerField(default=0, verbose_name="初始销量")
    sales_actual = models.IntegerField(default=0, verbose_name="实际销量")
    product_sort = models.IntegerField(default=0, verbose_name="商品排序")
    is_delete = models.BooleanField(default=False, verbose_name="是否删除")
    create_time = models.IntegerField(default=int(time.time()), verbose_name="创建时间")
    update_time = models.IntegerField(default=int(time.time()), verbose_name="更新时间")

    class Meta:
        db_table = 'bangtuitui_py_product'
        ordering = ['product_sort', '-create_time']
        verbose_name = "商品"
        verbose_name_plural = "商品"
        app_label = 'goods'

    def __str__(self):
        return self.product_name

    @property
    def product_sales(self):
        """计算商品显示销量"""
        return self.sales_initial + self.sales_actual

    def add(self, data):
        """添加商品"""
        if 'image' not in data or not data['image']:
            return False, '请上传商品图片'
        self.product_name = data.get('product_name')
        self.product_status = data.get('product_status', 10)
        self.product_stock = data.get('product_stock', 0)
        self.product_price = data.get('product_price', 0.0)
        self.create_user_id = data.get('create_user_id')
        self.grade_ids = ','.join(map(str, data.get('grade_ids', [])))
        self.save()
        # 添加商品图片
        # if 'image' in data:
        #     self.add_product_images(data['image'])
        # return True, "添加成功"

    # def add_product_images(self, images):
    #     """添加商品图片"""
    #     self.productimage_set.all().delete()  # 删除原有的图片
    #     for img in images:
    #         ProductImage.objects.create(
    #             product=self,
    #             image_id=img.get('file_id') or img.get('image_id'),
    #             app_id=self.app_id
    #         )

    def edit(self, data):
        """编辑商品"""
        if 'image' not in data or not data['image']:
            return False, '请上传商品图片'
        self.product_name = data.get('product_name', self.product_name)
        self.product_status = data.get('product_status', self.product_status)
        self.product_stock = data.get('product_stock', self.product_stock)
        self.product_price = data.get('product_price', self.product_price)
        self.update_time = timezone.now()
        self.save()
        # if 'image' in data:
        #     self.add_product_images(data['image'])
        # return True, "编辑成功"

    def set_status(self, state):
        """修改商品状态"""
        self.product_status = state
        self.save(update_fields=['product_status'])
        return True

    def set_delete(self):
        """软删除商品"""
        self.is_delete = True
        self.save(update_fields=['is_delete'])
        return True

    @staticmethod
    def get_product_total(filters=None):
        """获取当前商品总数"""
        return Product.objects.filter(is_delete=False, **(filters or {})).count()

    @staticmethod
    def get_product_stock_total():
        """获取商品告急数量总数"""
        return Product.objects.filter(is_delete=False, product_stock__lt=20).count()

    @staticmethod
    def get_list(params):
        """获取商品列表"""
        query = Product.objects.filter(is_delete=False)
        if 'product_name' in params:
            query = query.filter(product_name__icontains=params['product_name'])
        if 'product_status' in params:
            query = query.filter(product_status=params['product_status'])
        if 'category_id' in params:
            query = query.filter(category_id=params['category_id'])
        return query.order_by('product_sort', '-create_time')

    def get_many_spec_data(self, spec_rel, sku_data):
        """商品多规格信息处理（示例）"""
        spec_attr_data = []
        spec_list_data = []
        # 处理 spec_rel 和 sku_data，生成所需格式的数据
        # 该部分可以根据实际业务需求实现
        return {'spec_attr': spec_attr_data, 'spec_list': spec_list_data}

    # def tags(self):
    #     """获取商品标签"""
    #     return self.tags_set.all()

    @staticmethod
    def get_show_sku(product):
        """获取最低价 SKU"""
        return min(product.sku_set.all(), key=lambda sku: sku.product_price, default=None)

    def detail(self, product_id):
        """获取商品详情"""
        return Product.objects.filter(product_id=product_id, is_delete=False).select_related(
            'category', 'sku', 'image'
        ).first()
