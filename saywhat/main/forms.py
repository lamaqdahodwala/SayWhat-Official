import django.forms as forms
from django.contrib.auth.models import User
from . import models

class PostModelForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title', 'body']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input'}),
            'body': forms.Textarea(attrs={'class': 'textarea', 'rows': 10, 'cols': 10})
        }

        