from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Movie, Profile
from django.contrib.auth.models import User

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        username = User.objects.get(email=email)
        user = authenticate(username=username.username, password=password)
        # import pdb 
        # pdb.set_trace()
        if user is not None:
            login(request, user)
            return redirect('register')
        else:
            return render(request, 'login.html', {'error': 'Invalid login email or password'})
    else:
        return render(request, 'login.html')

def index(request):
    return HttpResponse("hello")
# Create your views here.



@login_required
def logout_view(request):
    logout(request)
    return redirect('login')