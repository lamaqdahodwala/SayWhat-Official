from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from traceback import print_exc
class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
    form_class = UserCreationForm
    
def view_account(req, user_id):
    try:
        user = User.objects.get(pk=user_id)
        return render(req, 'user.html', {'user': user})
    except Exception as e:
        print_exc()
        return render(req, 'user_not_found.html')
    
def view_posts(req, user_id):
    try:
        user = User.objects.get(pk=user_id)
        return render(req, 'view_all_posts_or_comments.html', {'user': user, 'item': 'posts'})
    except Exception as e:
        print_exc()
        return render(req, 'user_not_found.html')
    
def view_comments(req, user_id):
    try:
        user = User.objects.get(pk=user_id)
        return render(req, 'view_all_posts_or_comments.html', {'user': user, 'item': 'comments'})
    except Exception as e:
        print_exc()
        return render(req, 'user_not_found.html')