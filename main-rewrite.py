import discord
import time
from discord.ext import commands
from classi.Keywords import Keywords
from classi.Gif import Gif
from classi.Easteregg import Eastereggs
from classi.Embedd import Embedd
from classi.UserProfile import UserProfile

TOKEN = 'ODI0MjQ5MjU3ODQyMDQ5MDI0.YFsn8A.OYXFJaWDeV4VJeW6LRFkVSWrBrs'

client = commands.Bot(command_prefix="🍰")

@client.command(name = "ping")

async def cutegif(ctx) :

    await ctx.channel.send("pong")

@client.event

async def on_message(message) :

    print("[nuovo messaggio] " + time.strftime("[%H:%M]"))

@client.event

async def on_ready() :

    print("bot online")

client.run(TOKEN)