from django.shortcuts import render, redirect
from .forms import Myform
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout

def index(request):
    form = Myform()
    if request.method == "POST":
        username = request.POST['username']
        password1 = request.POST['password1']
        user = User.objects.create(username=username)
        user.set_password(password1)
        user.save()
        print("Registration Successful")
        return redirect('login')
    return render(request, "index.html", {'form': form})

def log_in(request):
    if request.method == "POST":
        uname2 = request.POST["uname2"]
        pass2 = request.POST["password2"]
        
        # Authenticate the user with correct field names
        user = authenticate(request, username=uname2, password=pass2)
        if user is not None:
            login(request, user)
            print("Login Successful")
            return redirect("dash")
        else:
            print("Invalid username or password")

    return render(request, "login.html")

def dash(request):
    a = request.user
    return render(request, "dashboard.html", {"a": a})

def log_out(request):
    logout(request)
    return redirect('login')

