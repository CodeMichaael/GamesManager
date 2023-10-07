import interactions
from interactions import OptionType, slash_option, slash_command

"""
You can intergrate the API into a bot here.

Example:

import discord
from discord.ext import commands
import requests

# Create a Discord bot instance
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def new_game(ctx, *args):
    # Construct a request to your Django API for the "new-game" command
    api_url = 'YOUR_API_URL_HERE'  # Replace with your Django API URL
    data = {
        "command": "new-game",
        # Add any command-specific parameters here based on your API
    }

    # Send the request to your Django API
    response = requests.post(api_url, json=data)

    if response.status_code == 200:
        await ctx.send("Successfully created a new game.")
    else:
        await ctx.send("Error creating a new game.")

@bot.command()
async def start_game(ctx, game_id, *players):
    # Construct a request to your Django API for the "start-game" command
    api_url = 'YOUR_API_URL_HERE'  # Replace with your Django API URL
    data = {
        "command": "start-game",
        "game_id": game_id,
        "players": list(players)
    }
    
    # Send the request to your Django API
    response = requests.post(api_url, json=data)

    if response.status_code == 200:
        await ctx.send("Successfully started the game.")
    else:
        await ctx.send("Error starting the game.")

@bot.command()
async def end_game(ctx, game_id):
    # Construct a request to your Django API for the "end-game" command
    api_url = 'YOUR_API_URL_HERE'  # Replace with your Django API URL
    data = {
        "command": "end-game",
        "game_id": game_id
    }
    
    # Send the request to your Django API
    response = requests.post(api_url, json=data)

    if response.status_code == 200:
        await ctx.send("Successfully ended the game.")
    else:
        await ctx.send("Error ending the game.")

@bot.command()
async def modify_stats(ctx, game_id, player, stat_to_modify, stat_data):
    # Construct a request to your Django API for the "modify-stats" command
    api_url = 'YOUR_API_URL_HERE'  # Replace with your Django API URL
    data = {
        "command": "modify-stat",
        "game_id": game_id,
        "player": player,
        "stat_to_modify": stat_to_modify,
        "stat_data": stat_data
    }
    
    # Send the request to your Django API
    response = requests.post(api_url, json=data)

    if response.status_code == 200:
        await ctx.send("Successfully modified the stat.")
    else:
        await ctx.send("Error modifying the stat.")

@bot.command()
async def get_stats(ctx, game_id, stat):
    # Construct a request to your Django API for the "get-stat" command
    api_url = 'YOUR_API_URL_HERE'  # Replace with your Django API URL
    data = {
        "command": "get-stat",
        "game_id": game_id,
        "stat": stat
    }
    
    # Send the request to your Django API
    response = requests.post(api_url, json=data)

    if response.status_code == 200:
        stats_data = response.json().get("Get stats request")
        await ctx.send(f"Stats for {stat}: {stats_data}")
    else:
        await ctx.send("Error fetching the stat.")

# Run the bot
bot.run('YOUR_DISCORD_BOT_TOKEN')
"""