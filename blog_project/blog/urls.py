from django.urls import path
from .views import PostListCreateView, PostDetailView, home, create_post

urlpatterns = [
    path('', home, name='home'),  
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('create/', create_post, name='create-post'),
]