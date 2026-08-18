from django import forms
from .models import Player, Tournament, Match


class PlayerForm(forms.ModelForm):

    class Meta:

        model = Player

        fields = [
            "first_name",
            "last_name",
            "email",
            "phone",
            "rating",
        ]

        widgets = {

            "first_name": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "last_name": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "phone": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "rating": forms.NumberInput(
                attrs={
                    "class": "form-control"
                }
            ),

        }

class TournamentForm(forms.ModelForm):

    class Meta:
        model = Tournament

        fields = [
            "name",
            "location",
            "start_date",
            "end_date",
            "description",
        ]

        widgets = {

            "name": forms.TextInput(attrs={"class": "form-control"}),

            "location": forms.TextInput(attrs={"class": "form-control"}),

            "start_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date"
                }
            ),

            "end_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date"
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4
                }
            ),

        }


class MatchForm(forms.ModelForm):

    class Meta:

        model = Match

        fields = [

            "tournament",

            "player1",

            "player2",

            "result",

            "round_number",

        ]


        widgets = {

            "tournament": forms.Select(
                attrs={
                    "class":"form-control"
                }
            ),

            "player1": forms.Select(
                attrs={
                    "class":"form-control"
                }
            ),

            "player2": forms.Select(
                attrs={
                    "class":"form-control"
                }
            ),

            "result": forms.Select(
                attrs={
                    "class":"form-control"
                }
            ),

            "round_number": forms.NumberInput(
                attrs={
                    "class":"form-control"
                }
            ),

        }