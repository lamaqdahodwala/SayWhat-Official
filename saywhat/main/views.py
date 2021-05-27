from django.shortcuts import render
from .forms import PostModelForm
from time import asctime
# Create your views here.
def index(req):
    return render(req, 'index.html')

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