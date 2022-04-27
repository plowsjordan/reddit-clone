from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError
from .models import Post, Vote
from .serializers import PostSerializer, VoteSerializer

# Create your views here.

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()   
    serializer_class = PostSerializer
    permissions_classes = (permissions.IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(poster=self.request.user)
        
class VoteCreate(generics.CreateAPIView):
    serializer_class = VoteSerializer
    permissions_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        post = Post.objects.get(pk=self.kwargs['pk'])
        return Vote.objects.filter(voter=user, post=post)

    
    def perform_create(self, serializer):
        user = self.request.user
        post = Post.objects.get(pk=self.kwargs['pk'])
        vote = Vote.objects.filter(voter=user, post=post)
       
        if vote:
            raise ValidationError('You have already voted on this post')
        serializer.save(voter=user, post=post)