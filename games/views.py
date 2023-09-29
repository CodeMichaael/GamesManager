from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import serializers
from rest_framework import status
from django.shortcuts import get_object_or_404

@api_view(["GET", "POST"])
def gamesapi(request):
    if request.data["command"]:
        if request.method == "POST":
            if cmd == "new-game":
                serializer = GamesManagerSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    host = serializer.validated_data["host"]
                    name = serializer.validated_data["game_name"]
                    stats = serializer.validated_data["stats"]
                    stats_data = serializer.validated_data["stats_data"]
                    maxplayers = serializer.validated_data["max_players"]
                    # What each statistic should contain. ^
                    if isinstance(stats, list) and isinstance(stats_data, dict):
                        instance = GamesManager(host=host, game_name=name, max_players=maxplayers, stats=stats, stats_data=stats_data, online_game=False)
                        return Response({"message": "Successfully created new game."}, status=200)
                        instance.save()
                    else:
                        return Response({'error': 'The "stats" variable must be a list, and the "stats_data" variable must be a dictionary.'}, status=status.HTTP_400_BAD_REQUEST)
            
            elif cmd == "start-game":
                serializer = StartGameSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    host = serializer.validated_data["host"]
                    gameid = serializer.validated_data["game_id"]
                    players = serializer.validated_data["players"]
                    filter = GamesManager.objects.filter(game_id=gameid)

                    if filter and isinstance(players, list):
                        if len(players) <= 2:
                            manager = GamesManager.objects.get(game_id=gameid)
                            manager.online_game = True
                            return Response({"message": "Started game successfully."}, status=200)
                            manager.save()
                        else:
                            return Response({'error': 'At least 2 or more players is required to start a game.'}, status=status.HTTP_400_BAD_REQUEST)

                    else:
                        return Response({'error': 'Either game id was not found or "players" variable is not a list.'}, status=status.HTTP_400_BAD_REQUEST)

            elif cmd == "end-game":
                serializer = EndGameSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    game_id = serializer.validated_data["game_id"]
                    filter = GamesManager.objects.filter(game_id=game_id)
                    if filter:
                        manager = GamesManager.objects.get(game_id=game_id)
                        manager.online_game = True
                        return Response({"message": "Ended game successfully."}, status=200)
                        manager.save()
                    else:
                        return Response({'error': 'Game ID not found.'}, status=status.HTTP_400_BAD_REQUEST)

            elif cmd == "modify-stat":
                serializer = ModifyStatSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    game_id = serializer.validated_data["game_id"]
                    player = serializer.validated_data["player"]
                    stat = serializer.validated_data["stat_to_modify"]
                    statdata = serializer.validated_data["stat_data"]

                    filter = GamesManager.objects.filter(game_id=game_id)
                    if filter and isinstance(statdata, dict):
                        manager = GamesManager.objects.get(game_id=game_id)
                        data = manager.stats_data
                        if stat in data:
                            del data[stat]
                            data[stat] = statdata
                            return Response({"message": "Successfully modified value."}, status=200)
                        else:
                            return Response({'error': 'Stat not found.'}, status=status.HTTP_400_BAD_REQUEST)
                    else:
                        return Response({'error': 'Either game ID not found or "statdata" isnt a dictionary.'}, status=status.HTTP_400_BAD_REQUEST)
            
            elif cmd == "get-stat":
                serializer = GetStatSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    game_id = serializer.validated_data["game_id"]
                    stat = serializer.validated_data["stat"]

                    filter = GamesManager.objects.filter(game_id=game_id)
                    if filter:
                        manager = GamesManager.objects.get(game_id=game_id)
                        data = manager.stats_data

                        if stat in data:
                            return Response({"Get stats request": data[stat]}, status=200)
                        else:
                            return Response({'error': 'Stat not found.'}, status=status.HTTP_400_BAD_REQUEST)
                    else:
                        return Response({'error': 'Game ID not found.'}, status=status.HTTP_400_BAD_REQUEST)

            elif cmd == "join-game":
                serializer = JoinGameSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    game_id = serializer.validated_data["game_id"]
                    username = serializer.validated_data["user"]

                    # You can add how you'd like players to join.





    else:
        return Response({'error': 'Missing "command" value.'}, status=status.HTTP_400_BAD_REQUEST)