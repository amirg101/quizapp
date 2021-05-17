from django import forms
from .models import Quiz
class QuizForm(forms.ModelForm):
    class Meta:
        model=Quiz
        fields='__all__'

from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class createUserForm(UserCreationForm):

    class Meta:
        model=User
        fields=['username','email','password1','password2']