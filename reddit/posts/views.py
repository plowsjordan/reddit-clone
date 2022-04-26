from django.shortcuts import render
from rest_framework import generics

# Create your views here.

class PostListView(generics.ListAPIView):
    model = Post
    template_name = 'posts/post_list.html'
