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
auto_enable_message_sniper_on_start = config.get('auto_enable_message_sniper_on_start')


bot = commands.Bot(command_prefix=prefix, self_bot=True)

bot.msgsniper = auto_enable_message_sniper_on_start


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
    
@bot.command(aliases=[])
async def msgsniper(ctx, msgsniperlol=None):
    await ctx.message.delete()
    if str(msgsniperlol).lower() == 'true' or str(msgsniperlol).lower() == 'on':
        bot.msgsniper = True
        await ctx.send('Message-Sniper is now **enabled**', delete_after=2)
    elif str(msgsniperlol).lower() == 'false' or str(msgsniperlol).lower() == 'off':
        bot.msgsniper = False
        await ctx.send('Message-Sniper is now **disabled**', delete_after=2)
        
@bot.event
async def on_message_delete(message):
    if message.author.id == bot.user.id:
        return
    if bot.msgsniper:
        # if isinstance(message.channel, discord.DMChannel) or isinstance(message.channel, discord.GroupChannel): \\ removed so people cant get you disabled
        if isinstance(message.channel, discord.DMChannel):
            attachments = message.attachments
            if len(attachments) == 0:
                message_content = "`" + str(discord.utils.escape_markdown(str(message.author))) + "`: " + str(
                    message.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
                await message.channel.send(message_content)
            else:
                links = ""
                for attachment in attachments:
                    links += attachment.proxy_url + "\n"
                message_content = "`" + str(
                    discord.utils.escape_markdown(str(message.author))) + "`: " + discord.utils.escape_mentions(
                    message.content) + "\n\n**Attachments:**\n" + links
                await message.channel.send(message_content)
    if len(bot.sniped_message_dict) > 1000:
        bot.sniped_message_dict.clear()
    if len(bot.snipe_history_dict) > 1000:
        bot.snipe_history_dict.clear()
    attachments = message.attachments
    if len(attachments) == 0:
        channel_id = message.channel.id
        message_content = "`" + str(discord.utils.escape_markdown(str(message.author))) + "`: " + str(message.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
        bot.sniped_message_dict.update({channel_id: message_content})
        if channel_id in bot.snipe_history_dict:
            pre = bot.snipe_history_dict[channel_id]
            post = str(message.author) + ": " + str(message.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
            bot.snipe_history_dict.update({channel_id: pre[:-3] + post + "\n```"})
        else:
            post = str(message.author) + ": " + str(message.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
            bot.snipe_history_dict.update({channel_id: "```\n" + post + "\n```"})
    else:
        links = ""
        for attachment in attachments:
            links += attachment.proxy_url + "\n"
        channel_id = message.channel.id
        message_content = "`" + str(discord.utils.escape_markdown(str(message.author))) + "`: " + discord.utils.escape_mentions(message.content) + "\n\n**Attachments:**\n" + links
        bot.sniped_message_dict.update({channel_id: message_content})


@bot.event
async def on_message_edit(before, after):
    if before.author.id == bot.user.id:
        return
    if bot.msgsniper:
        if before.content is after.content:
            return
        # if isinstance(before.channel, discord.DMChannel) or isinstance(before.channel, discord.GroupChannel): \\ removed so people cant get you disabled
        if isinstance(before.channel, discord.DMChannel):
            attachments = before.attachments
            if len(attachments) == 0:
                message_content = "`" + str(
                    discord.utils.escape_markdown(str(before.author))) + "`: \n\📑 | Before\n" + str(
                    before.content).replace("@everyone", "@\u200beveryone").replace("@here",
                                                                                    "@\u200bhere") + "\n\📑 | After\n" + str(
                    after.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
                await before.channel.send(message_content)
            else:
                links = ""
                for attachment in attachments:
                    links += attachment.proxy_url + "\n"
                message_content = "`" + str(
                    discord.utils.escape_markdown(str(before.author))) + "`: " + discord.utils.escape_mentions(
                    before.content) + "\n\n\📑 | Attachments:\n" + links
                await before.channel.send(message_content)
    if len(bot.sniped_edited_message_dict) > 1000:
        bot.sniped_edited_message_dict.clear()
    attachments = before.attachments
    if len(attachments) == 0:
        channel_id = before.channel.id
        message_content = "`" + str(discord.utils.escape_markdown(str(before.author))) + "`: \n**BEFORE**\n" + str(
            before.content).replace("@everyone", "@\u200beveryone").replace("@here",
                                                                            "@\u200bhere") + "\n**AFTER**\n" + str(
            after.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
        bot.sniped_edited_message_dict.update({channel_id: message_content})
    else:
        links = ""
        for attachment in attachments:
            links += attachment.proxy_url + "\n"
        channel_id = before.channel.id
        message_content = "`" + str(
            discord.utils.escape_markdown(str(before.author))) + "`: " + discord.utils.escape_mentions(
            before.content) + "\n\n\📑 | Attachments:\n" + links
        bot.sniped_edited_message_dict.update({channel_id: message_content})
        
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
  await ctx.message.channel.send("```Commands: \nstream <Status Message> - Changes your status to Streaming\nwatch <Status Message> - Sets your status to watching\ngame <Status Message> - Changes your status to Playing\nlisten <Status Message> - Sets your status to Listing to\nreset - Resets your status\nmsgsniper <on/off> - Turns on/off your message sniper\npurge <Amount> - Deletes your messages\nmassreact <emoji> <amount> - reacts on messages with the <amount> of messages and <emoji> you pick```")

bot.run(token, bot = False)


# YOU MAY GET BANNED USING THIS.
# DISCORD ToS WON'T ALLOW IT!
