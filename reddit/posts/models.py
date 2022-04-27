from functools import total_ordering
from turtle import title
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum 
from rest_framework import generics 

class Post (models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.title

class Vote (models.Model):
    list_display = ('post', 'user', 'vote_total', 'pub_date', 'id', 'title')
    voter = models.ForeignKey(User, on_delete=models.CASCADE)    
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    vote_total = models.IntegerField(default=1)
 
    def _str_(self):
        return self.list_display

    def vote_total(self):
        return Post.objects.filter(pk=self.id).aggregate(Sum('vote_total'))