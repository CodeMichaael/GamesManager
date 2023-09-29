from django.db import models
import random
generate_key = random.randint(10000000, 99999999)

class GamesManager(models.Model):
    host = models.TextField()
    game_id = models.IntegerField(default=generate_key)
    max_players = models.IntegerField()
    stats = [str]
    stats_data = {str: any}
    online_game = models.BooleanField(default=False)

class StartGame(models.Model):
    host = models.TextField()
    game_id = models.IntegerField()
    players = [str] # Has to be more than 2 players to start the game.

class EndGame(models.Model):
    game_id = models.IntegerField()

class ModifyStat(models.Model):
    game_id = models.TextField()
    player = models.TextField()
    stat_to_modify = models.TextField()
    stat_data = models.TextField()

class GetStat(models.Model):
    game_id = models.TextField()
    stat = models.TextField()

class JoinGame(models.Model):
    game_id = models.IntegerField()
    user = models.TextField()