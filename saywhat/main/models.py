from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Post(models.Model):
    op = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100)
    body = models.TextField()
    upvotes = models.ManyToManyField(User, related_name='likes')
    def get_total_likes(self):
        return self.upvotes.count()
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', args=[self.pk])
    
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name= models.CharField(max_length=300)
    body = models.CharField(max_length=1000)
    
    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)