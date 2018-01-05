from django.forms import ModelForm
from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields= ["username", "password"]

class SubmissionForm(forms.Form):
	answer = forms.CharField()
