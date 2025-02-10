from django.urls import path
from . import views

urlpatterns = [
    path('api/get-posts', views.LatestPostsView.as_view(), name='get-posts'),
    path('api/get-all-posts', views.PostListView.as_view(), name='get-all-posts'),
    path('api/create-post', views.PostListView.as_view(), name='create-post'),
    path('api/get-post/<int:post_id>', views.PostDetailView.as_view(), name='get-post'),
    path('api/delete-post/<int:post_id>', views.PostDetailView.as_view(), name='delete-post'),
    path('api/update-post/<int:post_id>', views.PostDetailView.as_view(), name='update-post'),
]