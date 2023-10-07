from rest_framework import serializers
from .models import *

class GamesManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = GamesManager
        fields = "__all__"

class StartGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = StartGame
        fields = "__all__"

class EndGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = EndGame
        fields = "__all__"

class ModifyStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModifyStat
        fields = "__all__"

class JoinGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = JoinGame
        fields = "__all__"

class GetStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = GetStat
        fields = "__all__"

