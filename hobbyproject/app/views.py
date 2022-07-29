from django.shortcuts import get_object_or_404, redirect, render
from .models import Post
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    return render(request, 'index.html')

def todo(request):
    if request.method == "GET":
        print(request.user)
        if not request.user.is_authenticated: 
            return render(request, 'todo.html')
        else: 
            posts = Post.objects.filter(user=request.user).order_by('-id')
            paginator = Paginator(posts, 7)
            pagenum = request.GET.get('page')
            posts = paginator.get_page(pagenum)
            return render(request, 'todo.html', {'posts':posts})
    elif request.method == "POST":
        post = Post()
        post.content = request.POST['todo']
        post.user = request.user
        post.time = timezone.now()
        if request.POST['start']: post.start_time = request.POST['start']
        if request.POST['end']: post.end_time = request.POST['end']
        post.save()
    return redirect('todo')

def others(request):
    users= User.objects.all()
    return render(request, 'others.html', {'users':users})

def detail(request, id):
    user = get_object_or_404(User, pk=id)
    posts = Post.objects.filter(user=user).order_by('-id')
    return render(request, 'user-detail.html', {'posts':posts})

def modify(request, id):
    if request.method == "GET":
        posts = Post.objects.filter(user=request.user).order_by('-id')
        return render(request, 'todo-modify.html', {'posts':posts, 'targetID':id})
    elif request.method == "POST":
        post = get_object_or_404(Post, pk=id)
        post.content = request.POST['todo']
        post.user = request.user
        post.time = timezone.now()
        if request.POST['start']:
            post.start_time = request.POST['start']
        if request.POST['end']:
            post.end_time = request.POST['end']
        post.save()
        return redirect('todo')
def delete(request, id):
    post = get_object_or_404(Post, pk=id)
    post.delete()
    return redirect('todo')

def done(request, id):
    post = get_object_or_404(Post, pk=id)
    if post.done: post.done = False
    else: post.done = True
    post.save()
    return redirect('todo')