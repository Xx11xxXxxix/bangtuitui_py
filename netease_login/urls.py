from django.urls import path
from . import views

urlpatterns = [
    path('netEase_login/', views.netEase_login, name='netEase_login'),
    path('check_status/', views.check_status, name='check_status'),
    path('get_user_info/', views.get_user_info, name='get_user_info'),
]