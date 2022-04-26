from rest_framework import serializers 
from .models import Post
from .models import Vote


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'url', 'poster', 'pub_date')
