from django.urls import path
from . import views


urlpatterns = [
    path('comment/<int:pk>/', views.CreateComment.as_view(), name="create_comment"),
    path('tag/<str:slug>/', views.PostsByTagListView.as_view(), name='tag_detail'),
    path('post/<str:slug>', views.PostDetail.as_view(), name='post_detail'),
    path('', views.BaseView.as_view(), name='home'),
    path('posts-list/', views.PostsListView.as_view(), name='posts_list'),
    path('search/', views.SearchPostsListView.as_view(), name='search'),
]
