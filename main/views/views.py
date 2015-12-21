from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from main.models import Player, PlayerMatch, PlayerSync, ChallongeTournament
from main.forms import UserForm, PlayerForm, SignInForm, PlayerSyncForm, TournamentForm
import challonge
from django.forms import formset_factory
from django.core.exceptions import ObjectDoesNotExist
import datetime
from dateutil import parser

#ranking stuff
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
#end ranking stuff


def home(request):
    return render(request, 'main/index.html', {})


def ranking(request):
    players = Player.objects.all().order_by("-elo")
    return render(request, 'main/ranking.html', {'players': players})


def player_form(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        player_form = PlayerForm(request.POST)
        if all((user_form.is_valid(), player_form.is_valid())):
            new_user = user_form.save()
            new_player = player_form.save(commit=False)
            new_player.user = new_user
            new_player.save()
            return HttpResponseRedirect('/playerform/')
    else:
        user_form = UserForm()
        player_form = PlayerForm()
    return render(request, 'main/player_form.html',
                  {'user_form': user_form, 'player_form': player_form})


def player_profile(request, name):
    #if request.user.is_authenticated():
    player = Player.objects.get(user=User.objects.get(username=name).id)

    matches = PlayerMatch.objects.filter(winner=player) | PlayerMatch.objects.filter(loser = player)
    matches = matches.order_by("created_at", "id")
    return render(request, "main/player_profile.html",
                  {'player': player, "matches": matches})


def tournament_update_data(updated_at):
    players = Player.objects.all()
    no_player = players.get(name = "no_player")

    tournaments = ChallongeTournament.objects.all().order_by("created_at")

    #map the id of player from players to its proper index of players
    players_key = {}
    i = 0
    for p in players:
        players_key[p.id] = i
        i += 1

    #reset elo rankings back to default
    for p in players_key.values():
        players[p].elo = 1200.0

    playerSyncsDict = {}
    matchesDict = {}
    for tournament in tournaments:
        playerSyncsDict[tournament.id] = PlayerSync.objects.filter(tournament=tournament)
        matchesDict[tournament.id] = PlayerMatch.objects.filter(tournament=tournament).order_by("created_at")
        
        for p in playerSyncsDict[tournament.id]:
            try:
                if p.player is not None:
                    p.begin_elo = players.get(id=p.player.id).elo
                else:
                    p.begin_elo = 0.0
            except Player.DoesNotExist:
                p.begin_elo = 0.0
            p.updated_at = updated_at
        
        #recalculate match data
        for p in matchesDict[tournament.id]:

            try:
                p.winner = playerSyncsDict[tournament.id].get(challonge_id=p.challonge_winner_id).player
            except Exception:
                p.winner = None
            try:
                p.loser = playerSyncsDict[tournament.id].get(challonge_id=p.challonge_loser_id).player
            except Exception:
                p.loser = None
            if p.loser is not None and p.winner is not None:
                p.old_winner_elo = players[players_key[p.winner.id]].elo
                p.old_loser_elo = players[players_key[p.loser.id]].elo

                winner_odds = getWinOdds(p.old_winner_elo, p.old_loser_elo)
                #loser_odds = getWinOdds(p.old_loser_elo, p.old_winner_elo)

                p.new_winner_elo = getNewElo(p.old_winner_elo, winner_odds, True, 20.0)
                p.new_loser_elo = getNewElo(p.old_loser_elo, winner_odds, False, 20.0)

                players[players_key[p.winner.id]].elo = p.new_winner_elo
                players[players_key[p.loser.id]].elo = p.new_loser_elo

                p.updated_at = updated_at
                players[players_key[p.winner.id]].updated_at = updated_at
                players[players_key[p.loser.id]].updated_at = updated_at

    #save everything that has been updated
    for tournament in tournaments:
        for p in playerSyncsDict[tournament.id]:
            p.save()
        
        for p in matchesDict[tournament.id]:
            p.save()
    for p in players:
        p.save()
    return True


def tournament_create_data(challonge, id, tournament, created_at):
    #no_player = Player.objects.get(name="no_player")
    matches_data = challonge.matches.index(id)
    matches_data2 = []
    playerSyncs_data = []
    #get match data and store into database
    #also get ordered list of players in terms of ranking (reversed)
    addLoser = False
    updated_at = datetime.datetime.now()
    i = 0
    for p in matches_data:
        identifier = p["identifier"]

        loserID = p["loser-id"]
        if loserID == None:
            continue
        winnerID = p["winner-id"]
        if winnerID == None:
            continue

        try:
            oldMatch = PlayerMatch.objects.filter(tournament=tournament).get(identifier=identifier)
            oldMatch.challonge_winner_id=winnerID
            oldMatch.challonge_loser_id=loserID
            oldMatch.updated_at=updated_at
            oldMatch.save()
            
        except PlayerMatch.DoesNotExist:
            newMatch = PlayerMatch(challonge_winner_id=winnerID, challonge_loser_id=loserID, tournament=tournament, identifier=identifier, created_at=created_at, updated_at=updated_at)
            newMatch.save()

        if addLoser == True or int(p["round"]) < 0:
            addLoser = True
            participant = challonge.participants.show(id, loserID)
            try:
                oldPlayerSync = PlayerSync.objects.filter(tournament=tournament).get(challonge_id=loserID)
                oldPlayerSync.challonge_name = participant["name"]
                oldPlayerSync.final_ranking = i
                oldPlayerSync.save()
                playerSyncs_data.append(oldPlayerSync)
                
            except PlayerSync.DoesNotExist:
                newPlayerSync = PlayerSync(tournament=tournament, challonge_id=loserID, challonge_name=participant["name"], final_ranking=i)
                newPlayerSync.save()
                playerSyncs_data.append(newPlayerSync)
            i += 1
            if (int(p["round"]) >= 0):
                participant = challonge.participants.show(id, winnerID)
                try:
                    oldPlayerSync = PlayerSync.objects.filter(tournament=tournament).get(challonge_id=winnerID)
                    oldPlayerSync.challonge_name = participant["name"]
                    oldPlayerSync.final_ranking = i
                    oldPlayerSync.save()
                    playerSyncs_data.append(oldPlayerSync)
                    
                except PlayerSync.DoesNotExist:
                    newPlayerSync = PlayerSync(tournament=tournament, challonge_id=winnerID, challonge_name=participant["name"], final_ranking=i)
                    newPlayerSync.save()
                    playerSyncs_data.append(newPlayerSync)
                i += 1

    #remove matches that aren't up-to-date and don't belong anymore
    deletedMatches = PlayerMatch.objects.filter(tournament=tournament).exclude(updated_at=updated_at).delete
    #playerSyncs_data.reverse()
    playerSync = PlayerSync.objects.filter(tournament=tournament).order_by('-final_ranking')

    #get actual ranking
    count = 1
    rank = 0
    group = 1
    countDown = 4
    getFirstFour = 4
    doubleTake = False
    for p in playerSync:
        if getFirstFour > 0:
            rank = count
            getFirstFour -= 1
        if countDown == 0:
            rank = count
            if doubleTake == True:
                doubleTake = False
            else:
                doubleTake = True
                group = group * 2
            countDown = group
        countDown -= 1
        count += 1
        p.final_ranking = rank
        p.save()
    

def tournament_details(request, id):
    updated_at = datetime.datetime.now()
    try:
        # Tell pychallonge about your [CHALLONGE! API credentials](http://api.challonge.com/v1).
        challonge.set_credentials("moomoomamoo", "ZGhkIWPh05JyAhwmQI1S8BqYBD7DieZsaKPePIYo")
        tournament_data = challonge.tournaments.show(id)
        sync = True
    except:
        # couldn't sync to challonge
        sync = False
    try:
        tournament = ChallongeTournament.objects.get(url=id)
        if sync == True and tournament.updated_at < parser.parse(tournament_data["updated-at"]):#,"YYYY-MM-DDThh:mm:ssTZD"):
            tournament.name=tournament_data["name"]
            tournament.updated_at = updated_at
            tournament.save()
            if tournament_update_data(updated_at):
                upToDate = True
            else:
                upToDate = False
    except ChallongeTournament.DoesNotExist:
        #should just 404
        moo="moo"
    playerSyncs = PlayerSync.objects.filter(tournament=tournament).order_by("final_ranking")

    if request.method == 'POST':
        PlayerSyncFormSet = formset_factory(PlayerSyncForm, extra = playerSyncs.count())
        playerSyncFormSet = PlayerSyncFormSet(request.POST, request.FILES)
        if playerSyncFormSet.is_valid():
            for (p, form) in zip(playerSyncs, playerSyncFormSet):
                try: 
                    p.player = form.cleaned_data['playerChoice']
                    p.save()
                except KeyError:
                    p.player = None
                    p.save()
                p.form = form
            tournament_update_data(updated_at)
    else:
        PlayerSyncFormSet = formset_factory(PlayerSyncForm, extra = playerSyncs.count())
        playerSyncFormSet = PlayerSyncFormSet()
        for (p, form) in zip(playerSyncs, playerSyncFormSet):
            form.fields["playerChoice"].initial = p.player
            p.form = form
    matches = PlayerMatch.objects.filter(tournament=tournament).order_by("created_at")
    return render(request, 'main/tournament_details.html', {'tournament': tournament, 'playerSyncs': playerSyncs, 'management_form': playerSyncFormSet.management_form})


def tournaments(request):
    if request.method == 'POST':
        form = TournamentForm(request.POST)
        if form.is_valid():
            challonge.set_credentials("moomoomamoo", "ZGhkIWPh05JyAhwmQI1S8BqYBD7DieZsaKPePIYo")
            url = form.cleaned_data['url']
            tournament_data = challonge.tournaments.show(url)
            name = tournament_data["name"]
            description = tournament_data["description"]
            created_at = tournament_data["created-at"]
            newTournament = ChallongeTournament(name=name,description=description,url=url,created_at=created_at,updated_at=created_at)
            newTournament.save()
            tournament_create_data(challonge, url, newTournament, created_at)
            tournament_update_data(datetime.datetime.now())
            #check if url is unqiue and if the tourney is completed
            #newTournament = ChallongeTournament(name=name, url=url, updated_at=updated_at)
            #tournament_update_data()
    else:
        form = TournamentForm()

    tournaments = ChallongeTournament.objects.all().order_by("created_at")
    i=2
    doit=True
    while(doit==True):
        try:
            tournaments.append(tournments[i])
            tournament[i] = None
            i += 3
        except:
            doit=False
    return render(request, 'main/tournaments.html', {'form': form, 'tournaments': tournaments})