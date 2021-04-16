import discord
import time
from discord.ext import commands
from classi.Keywords import Keywords
from classi.Gif import Gif
from classi.Easteregg import Eastereggs
from classi.Embedd import Embedd
from classi.UserProfile import UserProfile

Parole = Keywords()
gifs = Gif()
embed=discord.Embed()
embedd = Embedd()
profilo = UserProfile()

TOKEN = 'ODI0MjQ5MjU3ODQyMDQ5MDI0.YFsn8A.OYXFJaWDeV4VJeW6LRFkVSWrBrs'

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix="🍰", intents = intents)



@client.command(name = "gif")

async def cutegif( ctx ) :

    await ctx.channel.send("placeholder gif")

@client.command(name = "profile")

async def showProfile( ctx ) :

    profilo.NewUserProfile(ctx.author.id)
    await ctx.channel.send(embed = embedd.getUserProfile(ctx.author.id, profilo.cuteness, ctx.author.name))

@client.event

async def on_message(message) :

    if message.author.bot: return #blocks bot messages

    print("[nuovo messaggio] " + time.strftime("[%H:%M]")) #prints message infos

    await client.process_commands(message) #makes commands work 

@client.event

async def  on_member_join(member) :

    embedd.setGuildName(member.guild.name)
    embedd.setUserName(member.name)
    print(embedd.getUserName())
    await member.send(embed = embedd.welcomeMessage(gifs.getRandGifBenvenuto()))
    profilo.saveUserDatabase()

@client.event
async def on_ready() :

    print("------------")
    print(" bot online")
    print("------------")
    profilo.loadUserDatabase()

client.run(TOKEN)