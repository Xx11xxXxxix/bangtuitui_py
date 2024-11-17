from django.urls import path
from . import views

urlpatterns = [
    path('top-songs/', views.get_top_songs, name='top_songs'),
]

from django.urls import path, include

urlpatterns = [
    path('api/music/', include('music_api.urls')),
]