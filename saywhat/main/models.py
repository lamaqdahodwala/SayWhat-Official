from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    op = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100)
    body = models.TextField()
    
    def __str__(self):
        return self.title
