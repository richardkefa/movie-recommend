from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Movie, Profile
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm

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

def register_view(request):

    if request.method == "POST":

        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})
    #     try:
    #         email = request.POST['email']
    #         user_email = User.objects.get(email=email)
    #     except User.DoesNotExist:
    #         if user_email == User.DoesNotExist :
    #             return render(request, 'register.html', {'error': 'User Exists Try Login'})
    #         elif request.POST['password'] == request.POST['password2']:
    #             return render(request, 'register.html', {'error':'Password Did Not Match'})
    #         else:
    #             user = User.objects.create_user(
    #             email=request.POST['email'],
    #             password=request.POST['password'],
    #             first_name=request.POST['first_name'],
    #             username=request.POST['username'],
    #             last_name=request.POST['last_name'],
                
    #             )
    #             user.save()
    #             return redirect('login')  
    # else:
    #     return render(request, 'register.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('logout')