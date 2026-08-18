from django.db import models


class Player(models.Model):

    first_name = models.CharField(max_length=100)

    last_name = models.CharField(max_length=100)

    email = models.EmailField(unique=True)

    phone = models.CharField(max_length=20)

    rating = models.IntegerField(default=1200)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Tournament(models.Model):

    name = models.CharField(max_length=200)

    location = models.CharField(max_length=200)

    start_date = models.DateField()

    end_date = models.DateField()

    description = models.TextField(blank=True)


    def __str__(self):
        return self.name
    

class Match(models.Model):

    tournament = models.ForeignKey(
        Tournament,
        on_delete=models.CASCADE
    )

    player1 = models.ForeignKey(
        Player,
        related_name="player1_matches",
        on_delete=models.CASCADE
    )

    player2 = models.ForeignKey(
        Player,
        related_name="player2_matches",
        on_delete=models.CASCADE
    )

    result_choices = [

        ("Player 1 Win", "Player 1 Win"),

        ("Player 2 Win", "Player 2 Win"),

        ("Draw", "Draw"),

    ]

    result = models.CharField(
        max_length=20,
        choices=result_choices,
        default="Draw"
    )


    round_number = models.IntegerField(default=1)


    def __str__(self):
        return f"{self.player1} vs {self.player2}"