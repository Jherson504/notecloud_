from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .backend import update_json
from .models import Post, Topic, Comment

# Create your views here.
# auth


def authenticate_user(request):
    if request.user.is_authenticated:
        print("redirecting to logout page")
        return redirect('logout')

    return redirect('login')


def logout_page(request):
    if not request.user.is_authenticated:
        print("redirecting to login page")
        return redirect('login')
    logout(request)
    return redirect('home')
    # return render(request, 'base/logout.html')


def login_page(request):

    if request.user.is_authenticated:
        print("redirecting to homepage")
        return redirect('home')
    if request.method == 'POST':
        if request.POST.get('login'):
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                print("Logged in")
                return redirect('home')
            messages.error(request, 'Invalid password')
        elif request.POST.get('sign-in'):
            print("\n\n\n\n\n\nSign-in\n\n\n\n\n")
            username = request.POST.get('username')
            password = request.POST.get('password')
            new_user = User.objects.create(username=username)
            new_user.set_password(password)
            new_user.save()
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                print("Logged in")
                update_json()
                return redirect('home')

    users = User.objects.all()
    usernames = []
    for user in users:
        usernames.append(user)
    context = {
        'users': users,
        'usernames': usernames,
    }

    return render(request, 'base/login.html', context)


def home(request):
    posts = Post.objects.all()

    context = {
        'posts': posts
    }
    return render(request, 'base/home.html', context)


def edit_post(request, pk):
    post = Post.objects.get(id=pk)

    if request.method == 'POST':
        form = request.POST
        content = form.get('content')
        post.content = content

        post.save()

    context = {
        'post': post,
    }
    return render(request, 'base/post-edit.html', context)


def write_post(request):
    if request.method == 'POST':
        form = request.POST
        title = form.get('title')
        topic_name = form.get('topic')
        # print(title, topic_name)
        topic = Topic.objects.create(name=topic_name)
        post = Post.objects.create(
            title=title, topic=topic, owner=request.user)
        topic.save()
        post.save()
        return redirect('edit-post', pk=post.id)

    return render(request, 'base/post-write.html')
