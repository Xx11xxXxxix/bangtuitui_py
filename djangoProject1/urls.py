"""
URL configuration for djangoProject1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,include

import User_login
from accounts import views
from admin.denglu.views import PassportView
from admin.goods.GoodsView import ProductView, ProductDetailView, ProductStateView, get_base_data, RoleView
from captcha.views import captcha_image

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('user/', include('user.urls')),
    path('products/', ProductView.as_view(), name='product_list'),
    path('products/<int:product_id>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/<int:product_id>/state/<int:state>/', ProductStateView.as_view(), name='product_state'),
    path('products/base-data/', get_base_data, name='product_base_data'),
    path('denglu/login',PassportView.as_view(),name='login'),
    path('authRole/user/getRoleList', RoleView.as_view(), name='get_role_list'),
    path('netease/', include('netease_login.urls')),
    path('register/', views.register_user, name='register_user'),
    # 登录模块
    path('user_login/', include('User_login.urls')),

    path('captcha/', captcha_image, name='captcha'),

]
