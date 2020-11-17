from django.shortcuts import render, redirect, HttpResponse
from .models import User
from django.contrib import messages
import bcrypt

# Create your views here.

def index(request):
    return render(request, 'index.html')

# Register Route
def register(request):
    request.session.clear()
    request.session['reg'] = 1
    request.session['word'] = 'Registered'
    errors = User.objects.user_validation(request.POST)
    if len(errors) > 0:
        print(len(errors),'ERRORS!')
        for key, val in errors.items():
            print(key,val)
            messages.error(request, val)
        return redirect('/')
    else:
        print('No errors')
        pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        user = User.objects.create(
            first_name=request.POST['fname'],
            last_name=request.POST['lname'],
            email=request.POST['email'],
            password=pw_hash
        )
        request.session['user'] = user.id
        test = User.objects.get(id=user.id)
        print("first_name:",test.first_name, "last_name:",test.last_name, "email:",test.email, "password:",test.password)
    return redirect('/success')

# Login Route
def login(request):
    request.session.clear()
    request.session['log'] = 1
    request.session['word'] = 'Logged In'
    errors = User.objects.login_validation(request.POST)
    if len(errors) > 0:
        print(len(errors),'ERRORS!')
        for key, val in errors.items():
            print(key,val)
            messages.error(request, val)
        return redirect('/')
    else:
        print('No errors')
        user = User.objects.get(email=request.POST['email'])
        request.session['user'] = user.id
    return redirect('/success')

# Logged In/ Registered Route
def success(request):
    context = {
        'User': User.objects.get(id=request.session['user']),
        'status': request.session['word']
    }
    return render(request, 'success.html', context)

# Logout Route
def logout(request):
    request.session.clear()
    return redirect('/')