# services/product_service.py
from models.goods.CategoryModel import Category


class BaseProductService:
    """商品服务类，包含公共处理方法"""

    @staticmethod
    def get_spec_data(model=None):
        """
        获取商品规格数据
        :param model: 商品实例
        :return: 多规格数据或 False
        """
        if model and model.spec_type == 20:
            return model.get_many_spec_data(model.spec_rel.all(), model.sku.all())
        return False


class ProductService(BaseProductService):
    """商品服务类"""

    @staticmethod
    def get_edit_data(model=None, scene='edit'):
        """
        获取商品管理公共数据
        :param model: 商品模型实例
        :param scene: 场景类型，默认为 'edit'
        :return: 字典形式包含分类、配送模板、会员等级列表等数据
        """
        # 商品分类
        category = Category.get_cache_tree()

        # 配送模板
        # delivery = Delivery.get_all()

        # 会员等级列表
        # grade_list = Grade.get_usable_list()

        # 商品 SKU 数据
        spec_data = ProductService.get_spec_data(model)

        # 商品规格是否锁定
        is_spec_locked = ProductService.check_spec_locked(model, scene)

        return {
            'category': category,
            # 'delivery': delivery,
            # 'gradeList': grade_list,
            'specData': spec_data,
            'isSpecLocked': is_spec_locked
        }

    @staticmethod
    def check_spec_locked(model=None, scene='edit'):
        """
        检查商品规格是否被锁定
        :param model: 商品实例
        :param scene: 场景类型
        :return: bool
        """
        return False
