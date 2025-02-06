from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
from django.shortcuts import render, redirect
from django.http import HttpResponse

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    

def home(request):
    posts = Post.objects.all()  # Fetch all posts
    return render(request, 'blog/index.html', {'posts': posts})  # Pass posts to the template

def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Post.objects.create(title=title, content=content)  # Create a new post
        return redirect('home')  # Redirect to home after creating a post
    return render(request, 'blog/create_post.html')  # Render the post creation form