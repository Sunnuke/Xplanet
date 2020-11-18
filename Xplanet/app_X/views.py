from django.shortcuts import render, redirect, HttpResponse
from .models import *


# Create your views here.
def xplanet(request):
    return HttpResponse('Hi Human')

def forum(request):
    # context = {
    #     'User': User.objects.get(id=request.session['user']),
    #     'status': request.session['word'],
    #     'Posts': Post.objects.all()
    # }
    # return render(request, '', context)
    pass

def post(request):
    Post.objects.create(
        message=request.POST['post'],
        user=User.objects.get(id=request.session['user'])
    )
    # return redirect('')
    pass


def comment(request):
    Comment.objects.create(
        message=Post.objects.get(id=int(request.POST['comkey'])),
        user=User.objects.get(id=request.session['user']),
        comment=request.POST['comment']
    )
    # return redirect('')

def delete(request):
    c = Post.objects.get(id=request.POST['delkey'])
    c.delete()
    # return redirect('')
    pass
