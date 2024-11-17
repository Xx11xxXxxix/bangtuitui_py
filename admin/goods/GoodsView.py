# views.py
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework import status

from common.views import BaseController
from models.goods.CategoryModel import Category
from models.goods.GoodsModel import Product
from services.GoodsService import ProductService


class ProductView(BaseController):

    def get(self, request):
        """获取商品列表 (在售)"""
        user = request.user
        print(user)
        params = request.GET.dict()

        # 获取所有商品
        products = Product.objects.all()

        # 根据用户角色筛选商品数据
        if not user.is_super:
            if user.role_id == 1:
                pass  # 管理员
            elif user.role_id == 2:
                params['create_user_id'] = user.id  # 员工只能看到自己创建的商品
            else:
                return Response({'detail': '无权限查看数据'}, status=status.HTTP_403_FORBIDDEN)

        products = products.filter(**params)
        categories = Category.get_cache_tree()
        product_count = {
            'sell': products.filter(product_price=10).count(),
            'recovery': products.filter(product_price=30).count(),
            'lower': products.filter(product_price=20).count(),
        }

        return JsonResponse({
            'list': list(products.values()),
            'category': categories,
            'product_count': product_count,
        }, status=200)

    def post(self, request):
        """添加商品"""
        data = request.data.get('params', {})
        if request.query_params.get('scene') == 'copy':
            # 初始化复制商品的数据
            data['sales_initial'] = 0
            data.pop('create_time', None)
            data.pop('sku', {}).pop('product_sku_id', None)
            data.pop('product_sku', {}).pop('product_sku_id', None)
            if data.get('spec_type') == 20:
                for spec in data.get('spec_many', {}).get('spec_list', []):
                    spec['product_sku_id'] = 0

        product = Product(create_user_id=request.user.id)
        success, message = product.add(data)
        if success:
            return Response({'message': '添加成功'}, status=status.HTTP_201_CREATED)
        return Response({'message': message}, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailView(BaseController):

    def get(self, request, product_id):
        """获取商品详情"""
        product = Product.objects.filter(id=product_id).first()
        if not product:
            return Response({'message': '商品不存在'}, status=status.HTTP_404_NOT_FOUND)

        data = ProductService.get_edit_data(product)
        return Response(data, status=status.HTTP_200_OK)

    def put(self, request, product_id):
        """编辑商品"""
        product = Product.objects.filter(id=product_id).first()
        if not product:
            return Response({'message': '商品不存在'}, status=status.HTTP_404_NOT_FOUND)

        data = request.data.get('params', {})
        if product.edit(data):
            return Response({'message': '更新成功'}, status=status.HTTP_200_OK)
        return Response({'message': product.get_error() or '更新失败'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, product_id):
        """删除商品"""
        product = Product.objects.filter(id=product_id).first()
        if not product:
            return Response({'message': '商品不存在'}, status=status.HTTP_404_NOT_FOUND)

        if product.set_delete():
            return Response({'message': '删除成功'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'message': product.get_error() or '删除失败'}, status=status.HTTP_400_BAD_REQUEST)


class ProductStateView(BaseController):
    def post(self, request, product_id, state):
        """修改商品状态"""
        product = Product.objects.filter(id=product_id).first()
        if not product:
            return Response({'message': '商品不存在'}, status=status.HTTP_404_NOT_FOUND)

        if product.set_status(state):
            return Response({'message': '操作成功'}, status=status.HTTP_200_OK)
        return Response({'message': '操作失败'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_base_data(request):
    """获取商品基础数据"""
    data = ProductService.get_edit_data()
    return Response(data, status=status.HTTP_200_OK)
