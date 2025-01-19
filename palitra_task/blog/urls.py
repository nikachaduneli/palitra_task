from django.urls import path
from . import views


urlpatterns = [
    path('blogs/', views.BlogListCreateAPIView.as_view(), name='blog-list-create'),
    path('blogs/<int:pk>/', views.BlogRetrieveUpdateDestroyAPIView.as_view(), name='blog-detail'),

    path('blogs/<int:pk>/comments/', views.CommentListCreateAPIView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', views.CommentRetrieveUpdateDestroyAPIView.as_view(), name='comment-detail'),

    path('categories/', views.CategoryListAPIView.as_view(), name='category-list'),
    path('tags/', views.TagListAPIView.as_view(), name='tag-list'),
    path('menus/', views.MenuListAPIView.as_view(), name='menu-list'),
]