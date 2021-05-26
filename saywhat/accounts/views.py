from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('/')
    form_class = UserCreationForm