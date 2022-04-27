from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Post, Vote
from .serializers import PostSerializer, VoteSerializer

# Create your views here.

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()   
    serializer_class = PostSerializer
    permissions_classes = (permissions.IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(poster=self.request.user)

    def delete(self, request, *args, **kwargs):
        id = request.data.get('id')
        post = Post.objects.get(id=id)
        if post.poster == request.user:
            post.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        pass

        
class VoteCreate(generics.CreateAPIView):
    serializer_class = VoteSerializer
    permissions_classes = (permissions.IsAuthenticated)

    def get_queryset(self):
        user = self.request.username 
        post = Post.objects.get(pk=self.kwargs['pk'])
        return Vote.objects.filter(voter=user, post=post)