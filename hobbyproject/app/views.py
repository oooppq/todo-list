from django.shortcuts import get_object_or_404, redirect, render
from .models import Post
from django.contrib.auth.models import User
from django.utils import timezone

# Create your views here.
def home(request):
    return render(request, 'index.html')

def todo(request):
    if request.method == "GET":
        print(request.user)
        if request.user.is_authenticated:
            posts = Post.objects.filter(user=request.user)
            return render(request, 'todo.html', {'posts':posts})
        else: return render(request, 'todo.html')
    elif request.method == "POST":
        post = Post()
        post.content = request.POST['todo']
        post.user = request.user
        post.time = timezone.now()
        post.save()
    return redirect('todo')

def others(request):
    users= User.objects.all()
    return render(request, 'others.html', {'users':users})

def detail(request, id):
    user = get_object_or_404(User, pk=id)
    posts = Post.objects.filter(user=user)
    return render(request, 'user-detail.html', {'posts':posts})

def delete(request, id):
    post = get_object_or_404(Post, pk=id)
    post.delete()
    return None# return redirect('todo')