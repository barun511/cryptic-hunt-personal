from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .forms import UserForm, SubmissionForm
from django.contrib.auth.forms import UserCreationForm
from .models import Level, Submission
# TODO clean up all redundant things.
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
	return render(request, 'signup.html', {'form': form})

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
	if request.user.is_authenticated() and request.user.profile.level >= level_number: # if the user level isn't high enough to access this level
		current_level = get_object_or_404(Level, level_number=level_number) # then they will simply be redirected to play which redirects them to the latest unsolved level
		possible_answers = [current_level.answer1, current_level.answer2, current_level.answer3]
		if request.method == "GET":
			form = SubmissionForm()
			return render(request, 'level.html', {'level' : current_level, 'form' : form})
		else:
			form = SubmissionForm(request.POST)
			if form.is_valid():
				answer = form.cleaned_data.get('answer')
				submission = Submission()
				submission.level = current_level
				submission.user = request.user
				submission.submitted_answer = answer
				print(answer)
				print(current_level.answer1)
				if answer in possible_answers:
					submission.accepted = True
					request.user.profile.level = current_level.level_number+1 # This also has some problems - we need to make sure that levels 1 to 15 all exist.
					request.user.save()
					# requests.user.profle.level+=1 <-- This is INCORRECT, Preetha/Paul. Can you figure out what the potential issue is?
				else:
					submission.accepted = False
					# display "Wrong Answer, try again", or something of the sort to give feedback.
				submission.save()
				return redirect('play')
	else:
		return redirect('play')

