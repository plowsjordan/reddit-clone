from django.db import models
from django.contrib.auth.models import User
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
    id = models.AutoField(primary_key=True)
    voter = models.ForeignKey(User, on_delete=models.CASCADE)    
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    vote_total = models.IntegerField(default=0)
  
    class Meta:
        ordering = ['-vote_total']

    def __str__(self):
        return self.vote_total