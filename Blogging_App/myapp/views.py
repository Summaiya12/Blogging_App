from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from myapp import models
from .models import Posts
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='register')
def Index(request):
    context = {
        'posts': Posts.objects.all()
    }
    return render(request, 'index.html', context)


@login_required(login_url='register')
def About(request):
    return render(request, 'about.html')


@login_required(login_url='register')
def Blog(request):
    if request.method == 'POST':
        image = request.FILES.get('img')
        title = request.POST.get('title')
        content = request.POST.get('content')
        posts = models.Posts(title=title, content=content, image=image, author=request.user)
        posts.save()
        return redirect('home')

    return render(request, 'blog.html')


def Login(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        password = request.POST.get('upassword')
        userr = authenticate(request, username=name, password=password)
        if userr is not None:
            login(request, userr)
            return redirect('home')
        else:
            return redirect('login')

    return render(request, 'login.html')


def Register(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        email = request.POST.get('uemail')
        password = request.POST.get('upassword')
        newUser = User.objects.create_user(name, email, password)
        newUser.save()
        return redirect('login')
    return render(request, 'Register.html')


@login_required(login_url='register')
def Post(request):
    context = {
        'posts': Posts.objects.filter(author=request.user)
    }
    return render(request, 'post.html', context)


def signouts(request):
    logout(request)
    return redirect('login')
