from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from main.models import Player, PlayerMatch, Bracket
from main.forms import UserForm, PlayerForm, PlayerMatchForm, PlayerMatchForm2, SignInForm, BracketUpdateForm
from django.http import JsonResponse
from main.serializers import BracketSerializer
from rest_framework import generics


class BracketList(generics.ListCreateAPIView):
    queryset = Bracket.objects.all()
    serializer_class = BracketSerializer


class BracketDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bracket.objects.all()
    serializer_class = BracketSerializer


def getWinOdds(eloA, eloB):
    exA = (1 + 10 ** ((eloB - eloA) / 400)) ** -1
    return exA


def getNewElo(elo, ex, win, K):
    new_elo = elo
    if win == True:
        new_elo = elo + K * (2 - ex)
    else:
        new_elo = elo - K * (2 - ex)
    return new_elo


def home(request):
    return render(request, 'main/home.html', {})


def player_form(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        player_form = PlayerForm(request.POST)
        if all((user_form.is_valid(), player_form.is_valid())):
            new_user = user_form.save()
            new_player = player_form.save(commit=False)
            new_player.user = new_user
            new_player.save()
            return HttpResponseRedirect('/')
    else:
        user_form = UserForm()
        player_form = PlayerForm()
    return render(request, 'main/player_form.html',
                  {'user_form': user_form, 'player_form': player_form})


def player_match_form(request):
    if request.method == 'POST':
        player_match_form = PlayerMatchForm(request.POST)
        player_match_form2 = PlayerMatchForm2(request.POST)
        if all((player_match_form.is_valid(), player_match_form2.is_valid())):
            new_player_match = player_match_form.save(commit = False)
            wins = player_match_form2.cleaned_data["wins"]
            wins_needed = player_match_form2.cleaned_data['wins_needed']

            #update elo of players
            winner = new_player_match.winner
            loser = new_player_match.loser

            old_winner_elo = winner.elo
            old_loser_elo = loser.elo

            winner_odds = getWinOdds(old_winner_elo, old_loser_elo)
            loser_odds = getWinOdds(old_loser_elo, old_winner_elo)

            #consider what K should be
            #for now, K is 20 + bonus for winning
            #K = 20

            K = 20.0 + 20.0 * float(min([wins, wins_needed])) / float(wins_needed)#(float(min([wins, wins_needed])) / float(wins_needed))

            new_winner_elo = getNewElo(old_winner_elo, winner_odds, True, K)
            new_loser_elo = getNewElo(old_loser_elo, loser_odds, False, 20.0)

            Player.objects.filter(pk=winner.pk).update(elo = new_winner_elo)
            Player.objects.filter(pk=loser.pk).update(elo = new_loser_elo)

            new_player_match.winner_elo_delta = new_winner_elo - old_winner_elo
            new_player_match.loser_elo_delta = new_loser_elo - old_loser_elo

            new_player_match.save()
            return HttpResponseRedirect(str(K))
    else:
        player_match_form = PlayerMatchForm()
        player_match_form2 = PlayerMatchForm2()
    return render(request, 'main/player_match_form.html',
                  {'player_match_form': player_match_form, 'player_match_form2': player_match_form2})


def player_profile(request, id):
    #if request.user.is_authenticated():
    return render(request, "main/player_profile.html",
                  {'player': Player.objects.get(user=id)})

def bracket(request):
    bracketUpdateForm = BracketUpdateForm()
    #bracket = Bracket.objects.get(id = 1)

    #playerIdList = models.CommaSeparatedIntegerField(max_length = 255, blank = True, default = "")
    #resultsList = models.CommaSeparatedIntegerField(max_length = 255, blank = True, default = "")
    #resultsArray = bracket.resultsList.split(",")
    return render(request, 'main/bracket.html', )

def bracket_data(request):

    # do something with the your data
    data = {}
    bracket = Bracket.objects.get(id = 1)
    data = bracket.dataJSON
    return JsonResponse(data)
    
'''
def sign_in(request):
    error = ""
    if request.method == 'POST':
        sign_in_form = SignInForm(request.POST)
        if sign_in_form.is_valid():
            username = sign_in_form.cleaned_data["username"]
            password = sign_in_form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/home/')
            else:
                error = "Invalid username/password."
                form = SignInForm(initial={'username': request.POST.get('username')})
                # return HttpResponseRedirect('/sign_in/')
    elif request.method == 'GET':
        sign_in_form = SignInForm()
    else:
        return HttpResponseRedirect('/sign_in/')
    return render(request, "sign_in.html", {'sign_in_form': sign_in_form, 'error': error})


def sign_out(request):
    logout(request)
    return HttpResponseRedirect('/home/')


def sign_up(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/home/')
    elif request.method == 'POST':
        user_form = UserForm(request.POST)
        myuser_form = MyUserForm(request.POST)
        if all((user_form.is_valid(), myuser_form.is_valid())):
            new_user = user_form.save()
            new_myuser = myuser_form.save(commit=False)
            new_myuser.user = new_user
            new_myuser.save()
            return HttpResponseRedirect('/sign_in')
    else:
        user_form = UserForm()
        myuser_form = MyUserForm()
    return render(request, 'main/sign_up.html',
                  {'user_form': user_form, 'myuser_form': myuser_form})
'''