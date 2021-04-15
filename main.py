import os

os.system("pip install discord")
os.system("cls")

# dont change these credits cuz the tool is under MIT license :)

os.system("title " + "Made by water1597 on TikTok [-] https://github.com/WaterTheDev/Discord-Streaming-Status")


# change what ever the fuck u want under here just nothing from up here :)

import discord
from discord.ext import commands
import time


bot = commands.Bot(command_prefix=['stream ', 'Stream ', 'stream', 'Stream'], self_bot=True)




@bot.event
async def on_ready():
    print("Streaming status started!")
    await bot.change_presence(activity=discord.Streaming(name="@water1597 on tiktok is sooooooo cool :)", url="https://www.youtube.com/watch?v=hIYiovihEeU"))
# THIS ONLY WORKS WITH TWITCH AND YOUTUBE LINKS!



# do streamstop to stop the fake stream
@bot.command(aliases=["stop"])
async def close(ctx):
    await bot.close()
    print("Bot Closed")
    print("Closing in 10 seconds :)")
    time.sleep(10)


bot.run('TOKEN HERE', bot = False)
