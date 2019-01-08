from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

class UserForm():
    class Meta:
        model = User
        fields= ["username", "password", "email"]

class SubmissionForm(forms.Form):
	answer = forms.CharField()

class UserDetailForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(UserDetailForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'email')
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True