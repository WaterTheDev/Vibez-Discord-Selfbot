# oh ur checking the src?
# feel free!
# https://github.com/WaterTheDev/Discord-Streaming-Status
import os

os.system("pip install discord") # some mfs dont have pip installed lmfao
os.system("cls") # dont call me dumb if u use linux

# dont change these credits cuz the tool is under MIT license :)

os.system("title " + "Made by water1597 on TikTok [-] https://github.com/WaterTheDev/Discord-Streaming-Status")


# change what ever the fuck u want under here just nothing from up here :)


import discord
from discord.ext import commands
import time
import json

with open('config.json') as f:
    config = json.load(f)

token = config.get('token')
prefix = config.get('prefix')
streamurl = config.get('streamurl')

bot = commands.Bot(command_prefix=prefix, self_bot=True)


# THIS ONLY WORKS WITH TWITCH AND YOUTUBE LINKS!
# THIS ONLY WORKS WITH TWITCH AND YOUTUBE LINKS!
bot.remove_command('help')

@bot.event
async def on_ready():
    print("Streaming status started!")
    print("Prefix: "+ prefix)
# THIS ONLY WORKS WITH TWITCH AND YOUTUBE LINKS!

@bot.command(aliases=["streaming"])
async def stream(ctx, *, message):
    if ctx.message.author.id == bot.user.id:
        await ctx.message.delete()
        print("Status Changed.")
        stream = discord.Streaming(
            name=message,
            url=streamurl,
        )
        await bot.change_presence(activity=stream)

@bot.command(aliases=["playing"])
async def game(ctx, *, message):
    if ctx.message.author.id == bot.user.id:
        await ctx.message.delete()
        print("Status Changed.")
        game = discord.Game(
            name=message
        )
        await bot.change_presence(activity=game)
                   
@bot.command(aliases=["listen"])
async def listening(ctx, *, message):
    if ctx.message.author.id == bot.user.id:
        await ctx.message.delete()
        print("Status Changed.")
        await bot.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.listening,
                name=message,
            ))

@bot.command(aliases=["watch"])
async def watching(ctx, *, message):
    if ctx.message.author.id == bot.user.id:
        await ctx.message.delete()
        print("Status Changed.")
        await bot.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.watching,
                name=message
            ))

# do streamstop to stop the fake stream
@bot.command(aliases=["stop", "reset"])
async def close(ctx):
    if ctx.message.author.id == bot.user.id:
        await ctx.message.delete()
        await bot.change_presence(activity=None, status=discord.Status.dnd)
        print("Status reset")
        time.sleep(10)

@bot.command()
async def help(ctx):
  await ctx.message.delete()
  await ctx.message.channel.send("```Commands: \nstream <Status Message> - Changes your status to Streaming\nwatch <Status Message> - Sets your status to watching\ngame <Status Message> - Changes your status to Playing\nlisten <Status Message> - Sets your status to Listing to\nreset - Resets your status```")

bot.run(token, bot = False)


# YOU MAY GET BANNED USING THIS.
# DISCORD ToS WON'T ALLOW IT!
