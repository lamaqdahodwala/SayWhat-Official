from django.forms import ModelForm
from . import models
class PostModelForm(ModelForm):
    class Meta:
        model = models.Post
        fields = ['title', 'body']