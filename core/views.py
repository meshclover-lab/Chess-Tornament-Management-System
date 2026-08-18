from django.shortcuts import render, redirect

from .models import Player, Tournament, Match

from .forms import PlayerForm, TournamentForm, MatchForm



def dashboard(request):

    context = {

        "player_count": Player.objects.count(),

        "tournament_count": Tournament.objects.count(),

        "match_count": Match.objects.count(),

    }

    return render(
        request,
        "dashboard.html",
        context
    )



def player_list(request):

    players = Player.objects.all()

    context = {

        "players": players

    }

    return render(

        request,

        "players/player_list.html",

        context

    )



def add_player(request):

    if request.method == "POST":

        form = PlayerForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("players")


    else:

        form = PlayerForm()


    return render(

        request,

        "players/add_player.html",

        {
            "form": form
        }

    )

def tournament_list(request):

    tournaments = Tournament.objects.all()

    return render(
        request,
        "tournaments/tournament_list.html",
        {
            "tournaments": tournaments
        }
    )



def add_tournament(request):

    if request.method == "POST":

        form = TournamentForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("tournaments")


    else:

        form = TournamentForm()


    return render(
        request,
        "tournaments/add_tournament.html",
        {
            "form": form
        }
    )


def match_list(request):

    matches = Match.objects.all()

    return render(
        request,
        "matches/match_list.html",
        {
            "matches": matches
        }
    )



def add_match(request):

    if request.method == "POST":

        form = MatchForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("matches")

    else:

        form = MatchForm()


    return render(
        request,
        "matches/add_match.html",
        {
            "form": form
        }
    )


def standings(request):

    players = Player.objects.all()

    standings_data = []


    for player in players:

        points = 0


        matches = Match.objects.filter(
            player1=player
        ) | Match.objects.filter(
            player2=player
        )


        for match in matches:


            if match.result == "Draw":

                points += 0.5


            elif match.result == "Player 1 Win" and match.player1 == player:

                points += 1


            elif match.result == "Player 2 Win" and match.player2 == player:

                points += 1



        standings_data.append({

            "player": player,

            "points": points

        })


    standings_data = sorted(

        standings_data,

        key=lambda x: x["points"],

        reverse=True

    )


    return render(

        request,

        "standings.html",

        {

            "standings": standings_data

        }

    )