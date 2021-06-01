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
        user = req.user
        return render(req, 'user.html', {'user': user})
    except Exception as e:
        print_exc()
        return render(req, 'user_not_found.html')