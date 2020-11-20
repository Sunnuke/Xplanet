from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages


# Create your views here.

# WISE WELCOME_________
def xplanet(request):
    if 'user' in request.session:
        context = {
            'User': Profile.objects.get(id=request.session['user']),
            'status': request.session['word'],
        }
    else:
        context = {
            'No_user': "Not Signed In!"
        }
    return render(request, 'wisewelcome.html', context)

def no_user(request):
    return render(request, 'nouser.html')


# DASHBOARD PAGE FUNCTIONS________
def dashboard(request):
    if 'user' not in request.session:
        return redirect('/xplanet/no_user')
    context = {
        'User': Profile.objects.get(id=request.session['user']),
        'User_liked': Profile.objects.get(id=request.session['user']).posts_liked.all().order_by("-id"),
        'User_comments': Profile.objects.get(id=request.session['user']).profile_comments.all().order_by("-id"),
        'Posts': Profile.objects.get(id=request.session['user']).posts.all().order_by("-id"),
        'Following': Profile.objects.get(id=request.session['user']).following.all(),
        'Followers': Profile.objects.get(id=request.session['user']).followers.all(),
        'status': request.session['word']
    }
    return render(request, 'dashboard.html', context)


# FORUM PAGE FUNCTIONS _________
def forum(request):
    if 'user' not in request.session:
        return redirect('/xplanet/no_user')
    context = {
        'User': Profile.objects.get(id=request.session['user']),
        'status': request.session['word'],
        'Posts': Post.objects.all().order_by('-id')
    }
    return render(request, 'forum.html', context)

def post(request):
    request.session['word'] = 'post'
    errors = Post.objects.valid_post(request.POST)
    if len(errors) > 0:
        for key, val in errors.items():
            print(key)
            messages.error(request, val)
        return redirect('/xplanet/forum')
    else:
        Post.objects.create(
            title=request.POST['title'],
            post=request.POST['post'],
            profile=Profile.objects.get(id=request.session['user'])
        )
    return redirect('/xplanet/forum')

def editpost(request):
    request.session['word'] = 'post'
    errors = Post.objects.valid_post(request.POST)
    if len(errors) > 0:
        for key, val in errors.items():
            messages.error(request, val)
        return redirect('/xplanet/forum')
    else:
        post = Post.objects.get(id=request.POST['postID'])
        post.post=request.POST['post']
        post.title=request.POST['title']
        post.save()
    return redirect('/xplanet/forum')

def comment(request):
    request.session['word'] = 'comment'
    errors = Comment.objects.valid_comment(request.POST)
    if len(errors) > 0:
        for key, val in errors.items():
            messages.error(request, val)
        return redirect('/xplanet/forum')
    else:
        Comment.objects.create(
            post=Post.objects.get(id=request.POST['comkey']),
            profile=Profile.objects.get(id=request.session['user']),
            comment=request.POST['comment']
        )
    return redirect('/xplanet/forum')

def delete(request):
    c = Post.objects.get(id=request.POST['delkey'])
    c.delete()
    return redirect('/xplanet/forum')

# Settings Page
def settings(request):
    if 'user' not in request.session:
        return redirect('/xplanet/no_user')
    context = {
        'User': Profile.objects.get(id=request.session['user']),
        'Following': Profile.objects.get(id=request.session['user']).following.all(),
        'Followers': Profile.objects.get(id=request.session['user']).followers.all(),
        'status': request.session['word']
    }
    return render(request, 'settings.html', context)

def update(request):
    errors = Profile.objects.valid_pro(request.POST)
    if len(errors) > 0:
        for key, val in errors.items():
            messages.error(request, val)
        return redirect('/success')
    else:
        profile = Profile.objects.get(id=request.session['user'])
        profile.name=request.POST['name']
        profile.bio=request.POST['bio']
        profile.save()
    return redirect('/xplanet/settings')