from django.urls import path

from . import views



urlpatterns = [

    path(
        "",
        views.dashboard,
        name="dashboard"
    ),


    path(
        "players/",
        views.player_list,
        name="players"
    ),


    path(
        "players/add/",
        views.add_player,
        name="add_player"
    ),

    path(
    "tournaments/",
    views.tournament_list,
    name="tournaments"
),


path(
    "tournaments/add/",
    views.add_tournament,
    name="add_tournament"
),


path(
    "matches/",
    views.match_list,
    name="matches"
),

path(
    "matches/add/",
    views.add_match,
    name="add_match"
),

path(
    "standings/",
    views.standings,
    name="standings"
),

]