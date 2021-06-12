from django.urls import path
from . import views


urlpatterns = [
    path('', views.BaseView.as_view(), name='home'),
    path('posts-list/', views.PostsListView.as_view(), name='posts_list'),
    path('post/<str:slug>', views.PostDetail.as_view(), name='post_detail'),
    path('search/>', views.SearchPostsListView.as_view(), name='search'),
]
