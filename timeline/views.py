from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import SignupForm, LoginForm, PostForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = SignupForm()
    param = {
        'form': form
    }
    return render(request, 'timeline/signup.html', param)

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user:
                login(request, user)
                return redirect('post_list')
    else:
        form = LoginForm()
    param = {
        'form': form,
    }
    return render(request, 'timeline/login.html', param)

def logout_view(request):
    logout(request)
    return render(request, 'timeline/logout.html')

def user_view(request):
    user = request.user
    params = {
        'user': user
    }
    return render(request, 'timeline/user.html', params)

def other_view(request):
    users = User.objects.exclude(username=request.user.username)
    params = {
        'users': users
    }
    return render(request, 'timeline/other.html', params)

def profile_view(request, user_id):
    user = User.objects.get(id=user_id)
    params = {
        'user': user
    }
    return render(request, 'timeline/profile.html', params)

def post_list(request):
    posts = Post.objects.order_by('-created_at')
    return render(request, 'timeline/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'timeline/post_detail.html', {'post': post})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'timeline/post_edit.html', {'form': form})
