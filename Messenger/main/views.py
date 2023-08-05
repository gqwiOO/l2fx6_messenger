from django.http import HttpResponse
from django.shortcuts import render
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth import authenticate, login

# Create your views here.

def index(request):
    return render(request, "main.html")

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, "logged_successfully.html")
                else:
                    return HttpResponse("Authenticated failed")
            else:
                return HttpResponse("Invalid login")
    else:
        form = LoginForm
    return render(request, 'login.html', {'form': form})

def user_registration(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return render(request, "registrated.html", {'new_user': user_form})
        else:
            return render(request, "error_registrated.html")
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration.html', {"user_form": user_form})
