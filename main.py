# oh ur checking the src?
# feel free!
# https://github.com/WaterTheDev/Discord-Streaming-Status
import os

#os.system("pip install discord.py") # some mfs dont have pip installed lmfao
#os.system("cls") # dont call me dumb if u use linux

# dont change these credits cuz the tool is under MIT license :)

os.system("pip install discord.py && cls && title Made by water1597 on TikTok [-] https://github.com/WaterTheDev/Discord-Streaming-Status")


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
    print("Vibez Selfbot started!")
    print("Prefix: "+ prefix)
# THIS ONLY WORKS WITH TWITCH AND YOUTUBE LINKS!

@bot.command(aliases=["streaming"])
async def stream(ctx, *, message):
    await ctx.message.delete()
    print("Status Changed.")
    stream = discord.Streaming(
        name=message,
        url=streamurl,
    )
    await bot.change_presence(activity=stream)

@bot.command(aliases=["playing"])
async def game(ctx, *, message):
    await ctx.message.delete()
    print("Status Changed.")
    game = discord.Game(
        name=message
    )
    await bot.change_presence(activity=game)
                   
@bot.command(aliases=["listen"])
async def listening(ctx, *, message):
    await ctx.message.delete()
    print("Status Changed.")
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening,
            name=message,
        ))

@bot.command(aliases=["watch"])
async def watching(ctx, *, message):
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
    await ctx.message.delete()
    await bot.change_presence(activity=None, status=discord.Status.dnd)
    print("Status reset")
    time.sleep(10)
    
@bot.command(aliases=["del", "cls"])
async def purge(ctx, amount: int = None):
    await ctx.message.delete()
    if amount is None:
        async for message in ctx.message.channel.history(limit=999).filter(lambda m: m.author == bot.user).map(
                lambda m: m):
            try:
                await message.delete()
            except:
                pass
    else:
        async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == bot.user).map(
                lambda m: m):
            try:
                await message.delete()
            except:
                pass
            
@bot.command(aliases=["react"])
async def massreact(ctx, emote, amount: int = None):
    await ctx.message.delete()
    messages = await ctx.message.channel.history(limit=amount).flatten()
    for message in messages:
        await message.add_reaction(emote)


@bot.command(aliases=["cmds"])
async def help(ctx):
  await ctx.message.delete()
  await ctx.message.channel.send("```Commands: \nstream <Status Message> - Changes your status to Streaming\nwatch <Status Message> - Sets your status to watching\ngame <Status Message> - Changes your status to Playing\nlisten <Status Message> - Sets your status to Listing to\nreset - Resets your status\npurge <Amount> - Deletes your messages\nmassreact <emoji> <amount> - reacts on messages with the <amount> of messages and <emoji> you pick```")

bot.run(token, bot = False)


# YOU MAY GET BANNED USING THIS.
# DISCORD ToS WON'T ALLOW IT!
