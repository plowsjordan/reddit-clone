from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer

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

        