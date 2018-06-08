from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .forms import UserForm, SubmissionForm
from django.contrib.auth.forms import UserCreationForm
from .models import Level, Submission, Profile
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
    ranked_list = Profile.objects.order_by('-level','time_of_level')
    return render(request, 'leaderboard.html', {'ranked_list' : ranked_list})

def play(request):
    if request.user.is_authenticated():
        return level(request, request.user.profile.level)
    else:
        return redirect('index')

def level(request, level_number):
    print(level_number)
    print(len(Level.objects.all()))
    if int(level_number) >= len(Level.objects.all()):
        return render(request, 'finished.html', {})
    if request.user.is_authenticated() and request.user.profile.level >= int(level_number): # if the user level isn't high enough to access this level
        current_level = get_object_or_404(Level, level_number=level_number) # then they will simply be redirected to play which redirects them to the latest unsolved level
        possible_answers = [current_level.answer1, current_level.answer2, current_level.answer3]
        acccessible_levels = Level.objects.filter(level_number=request.user.profile.level)
        if request.method == "GET":
            form = SubmissionForm()

            return render(request, 'level.html', {'userlevel' : request.user.profile.level, 'level' : current_level, 'form' : form})
        else:
            form = SubmissionForm(request.POST)
            if form.is_valid():
                answer = form.cleaned_data.get('answer')
                submission = Submission()
                submission.level = current_level
                submission.user = request.user
                submission.submitted_answer = answer
                print(submission)
                # todo make user.profile.level a level object instead of a level number really important and tricky to do do not forget or skip it
                # is this even possible with current architecture?
                if answer in possible_answers:
                    submission.accepted = True
                    # The level numbers represent some fundamental ordering of the levels, they should not be messed with.
                    
                    #request.user.profile.level = max(request.user.profile.level, current_level.level_number+1) # This also has some problems - we need to make sure that levels 1 to 15 all exist.
                    # max because we don't want to reduce her level if she just resolved a previous level.
                    # we only want to save if the level just solved has been solved for the first time.
                    # there are two ways to check this - first look at all submissions for _this_ level by _this_ user, and see how many accepted submissions there are
                    # if there is only one then we can save the user level, otherwise no need to update it.
                    #
                    # Old barun - you are stupid and this is needlessly complex. You just need to check if the user level 
                    # (which is defined as the maximum possible level the user can access)
                    # is equal to the current level or not. If it is, we can update it to the next level, otherwise
                    # the user is solving an earlier level and we don't need to update anything. 

                    '''
                    accepted_submissions_for_this_level = Submission.objects.filter(user__exact=request.user,level=current_level,accepted=True)
                    if (len(accepted_submissions_for_this_level) == 1):
                        request.user.save()
                    return redirect('level', current_level.level_number + 1)
                    '''
                    if (request.user.profile.level == current_level.level_number):
                        request.user.profile.level = current_level.level_number + 1
                        request.user.save()
                    return redirect('level', current_level.level_number + 1)
                    # requests.user.profle.level+=1 <-- This is INCORRECT, Preetha/Paul. Can you figure out what the potential issue is?
                else:
                    print("XD")
                    submission.accepted = False
                    return redirect('level', request.user.profile.level)
                    # display "Wrong Answer, try again", or something of the sort to give feedback.
                submission.save()
                
    else:
        print("XASD")
        return redirect('play')

