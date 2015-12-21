from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from main.models import Player, PlayerMatch, ChallongeTournament


class UserForm(UserCreationForm):
    model = User
    fields = ['username', 'password']


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name']


class PlayerSyncForm(forms.Form):
    playerChoice = forms.ModelChoiceField(queryset=Player.objects.order_by('name'), label="Player Sync", required=False)


class TournamentForm(forms.Form):
   url = forms.CharField(max_length=30)


class SignInForm(forms.Form):
    username = forms.CharField(label='Username', max_length=30)
    password = forms.CharField(label='Password', max_length=30, widget=forms.PasswordInput)