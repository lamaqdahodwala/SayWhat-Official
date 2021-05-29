from django.shortcuts import render, get_object_or_404
from .forms import PostModelForm, CommentModelForm
from time import asctime
from django.http import HttpResponseRedirect
from .models import Post
from django.views.generic import ListView, UpdateView


class ListPostView(ListView):
    model = Post
    template_name = 'index.html'
    
def new_post(req):
    if req.method == 'POST':
        form = PostModelForm(req.POST or None)
        instance = form.save(commit=False)
        instance.op = req.user
        instance.save()
        return HttpResponseRedirect('/')
    else:
        form = PostModelForm(instance=req.user)
        return render(req, 'newpost.html', {'form': form})
    
def view_post(req, key):
    post = Post.objects.get(pk=key)
    total_likes = post.get_total_likes()
    return render(req,'post.html', {'post': post, 'total_likes': total_likes})

def like_post(req, pk):
    post = get_object_or_404(Post, id=req.POST.get('post_id'))
    post.upvotes.add(req.user)
    post.save()
    return HttpResponseRedirect(f'/post/{pk}')

def new_comment(req, pk):
    post = get_object_or_404(Post, id=req.POST.get('post_id'))
    form = CommentModelForm(req.POST or None)
    instance = form.save(commit=False)
    instance.name = req.user.username
    instance.post = post
    instance.save()
    return HttpResponseRedirect(f'/post/{pk}')