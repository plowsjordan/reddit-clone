from django.shortcuts import render
from reddit.posts import serializers
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

# Create your views here.

class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()   
    serializers_class = PostSerializer

