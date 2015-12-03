from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from main.models import Player, PlayerMatch


class UserForm(UserCreationForm):
    model = User
    fields = ['username', 'password']


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['tag']


class PlayerMatchForm(forms.ModelForm):
    class Meta:
        model = PlayerMatch
        fields = ['winner', 'loser']

class PlayerMatchForm2(forms.Form):
    wins = forms.IntegerField(min_value = 0)
    wins_needed = forms.IntegerField(min_value = 1)


class BracketUpdateForm(forms.Form):
    player1name = forms.CharField(label='player1name', max_length=30)
    player2name = forms.CharField(label='player2name', max_length=30)


class UserForm(UserCreationForm):
    model = User
    fields = ['winner', 'loser']


class SignInForm(forms.Form):
    username = forms.CharField(label='Username', max_length=30)
    password = forms.CharField(label='Password', max_length=30, widget=forms.PasswordInput)