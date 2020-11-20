from django.shortcuts import render, redirect, HttpResponse
from .models import *


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
    Post.objects.create(
        message=request.POST['post'],
        user=User.objects.get(id=request.session['user'])
    )
    return redirect('/xplanet/forum')

def comment(request):
    Comment.objects.create(
        message=Post.objects.get(id=int(request.POST['comkey'])),
        user=User.objects.get(id=request.session['user']),
        comment=request.POST['comment']
    )
    return redirect('/xplanet/forum')

def delete(request):
    c = Post.objects.get(id=request.POST['delkey'])
    c.delete()
    return redirect('/xplanet/forum')
