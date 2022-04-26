from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post (models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-pub_date']


class Vote (models.Model):
    voter = models.ForeignKey(User, on_delete=models.CASCADE)    
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
  
