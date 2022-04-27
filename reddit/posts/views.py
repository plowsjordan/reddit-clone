from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, permissions, mixins, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import exception_handler
from .models import Post, Vote
from .serializers import PostSerializer, VoteSerializer
from . import urls

# Create your views here.

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()   
    serializer_class = PostSerializer
    permissions_classes = (permissions.IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(poster=self.request.user)
 
class PostRetrieveDestroy(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()   
    serializer_class = PostSerializer
    permissions_classes = (permissions.IsAuthenticatedOrReadOnly)

    def delete(self, request, *args, **kwargs):
        post = Post.objects.filter(pk=kwargs['pk'], poster=self.request.user)
        if post.exists():
            return self.destroy(request, *args, **kwargs)
        else:
            raise ValidationError('You cant delete this post')
        

class PostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()   
    serializer_class = PostSerializer
    permissions_classes = (permissions.IsAuthenticatedOrReadOnly)

    def delete(self,request, *args, **kwargs):
        post = Post.objects.filter(pk=kwargs['pk'], poster=self.request.user)
        if post.exists():
            return self.destroy(request, *args, **kwargs)
        else:
            raise ValidationError('You already deleted this post')



class VoteCreate(generics.CreateAPIView, mixins.DestroyModelMixin):
    serializer_class = VoteSerializer
    permissions_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        post = Post.objects.get(pk=self.kwargs['pk'])
        return Vote.objects.filter(voter=user, post=post)

    
    def perform_create(self, serializer):
        if self.get_queryset().exists():
            raise ValidationError('You have already voted on this post')
        serializer.save(voter=self.request.user, post=Post.objects.get(pk=self.kwargs['pk']))

    def delete(self, request, *args, **kwargs):
        if self.get_queryset().exists():
            self.get_queryset().delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise ValidationError('You have not voted on this post.. You can only delete your vote')


def index(request):
    return HttpResponse(" Welcome to the Reddit API Clone")