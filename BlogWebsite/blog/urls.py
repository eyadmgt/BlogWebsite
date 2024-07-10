from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('users/', views.users, name='users'),
    path('posts/', views.posts, name='posts'),
    path('comments/', views.comments, name='comments'),
    path('categories/', views.categories, name='categories'),
    path('posts/blog_details/<int:id>/', views.blog_details, name='blog_details'),
]
