from django.urls import path
from . import views
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'), #post_newというビューを探す。pkという名前の変数でビューに渡す。
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]



#今回使うURLの設定。各ビューの関数(post_newなど))を探し、変数を渡している。
