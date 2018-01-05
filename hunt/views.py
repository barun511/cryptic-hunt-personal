from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .forms import UserForm, 
from django.contrib.auth.forms import UserCreationForm
from .models import Level, Submission

# Create your views here.
def index(request):
    form = UserForm()# redundant
    return render(request, 'index.html', {'form': form})

def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=raw_password)
			return redirect('login')
	else:
		form = UserCreationForm()
	return render(requests, 'signup.html', {'form': form})

def base(request):
    return render(request, 'base.html', {})

def leaderboard(request):
    return render(request, 'leaderboard.html', {})

def play(request):
    if request.user.is_authenticated():
	    return level(request, request.user.profile.level)
    else:
        return redirect('index')

def level(request, level_number):
	if request.user.is_authenticated():
		current_level = get_object_or_404(Level, level_number=level_number)
		if requests.method == "GET" :
		return render(request, 'level.html', {'level' : current_level})
	else:
		return redirect('index')

