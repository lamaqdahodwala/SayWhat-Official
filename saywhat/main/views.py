from django.shortcuts import render
from .forms import PostModelForm
from time import asctime
from .models import Post
from django.views.generic import ListView, DetailView

# Create your views here.
class ListPostView(ListView):
    model = Post
    template_name = 'index.html'
    
def new_post(req):
    if req.method == 'POST':
        form = PostModelForm(req.POST or None)
        instance = form.save(commit=False)
        instance.op = req.user
        instance.save()
        return render(req, 'index.html')
    else:
        form = PostModelForm(instance=req.user)
        return render(req, 'newpost.html', {'form': form})
    
def view_post(req, key):
    post = Post.objects.get(pk=key)
    return render(req,'post.html', {'post': post})