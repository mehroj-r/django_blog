from django.urls import path
from . import views

urlpatterns = [
    path('api/getPosts', views.getPosts, name='getPosts'),
    path('api/getAllPosts', views.getAllPosts, name='getAllPosts'),
    path('api/createPost', views.createPost, name='createPost'),
    path('api/getPost/<int:id>', views.getPost, name='getPost'),
    path('api/deletePost/<int:id>', views.deletePost, name='deletePost'),
    path('api/updatePost/<int:id>', views.updatePost, name='updatePost'),
]