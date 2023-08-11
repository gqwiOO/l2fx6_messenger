from django.http import HttpResponse
from django.shortcuts import render
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth import authenticate, login
from django_currentuser.middleware import (get_current_user,get_current_authenticated_user)
from .models import Room
from django.contrib.auth.models import User

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

def messenger(request):
    user_rooms = Room.objects.all()
    return render(request, "messenger.html", context={"rooms": user_rooms})

def create_room(request):
    if request.method == "POST":
        room = Room()
        room.creator = get_current_user()
        room.member = User.objects.filter(username=request.POST.get("member"))[0]
        room.save()


    else:
        return render(request, "create_room.html")
    return render(request, "messenger.html")

def chat(request, room_id):
    return render(request, "chat.html", context={"room": Room.objects.filter(creator_id=get_current_user().id)})
