import discord
import time
import atexit
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

#exit thingy , it works , dont touch it

def exit_handler():
    profilo.saveUserDatabase()

atexit.register(exit_handler)

#exit thingy , it works , dont touch it

#start of commands

@client.command(name = "gif")

async def cutegif( ctx ) :

    await ctx.channel.send("placeholder gif")

@client.command(name = "profile")

async def showProfile( ctx ) :

    profilo.NewUserProfile(ctx.author.id)
    await ctx.channel.send(embed = embedd.getUserProfile(ctx.author.id, profilo.cuteness, ctx.author.name))
    print(profilo.getUserProfile())

@client.command(name = "cuteness")

#end of commands



@client.event #message handler uwu

async def on_message(message) :

    if message.author.bot: return #blocks bot messages

    print("[nuovo messaggio] " + "["+ message.guild.name + "] " + time.strftime("[%H:%M]")) #prints message infos

    profilo.NewUserProfile(message.author.id)

    if "im cute" in message.content :

        profilo.addSelfCuteness(message.author.id)

    await client.process_commands(message) #makes commands work 



@client.event

async def  on_member_join(member) :

    embedd.setGuildName(member.guild.name)
    embedd.setUserName(member.name)
    print(embedd.getUserName())
    await member.send(embed = embedd.welcomeMessage(gifs.getRandGifBenvenuto()))
    profilo.NewUserProfile(member.id)

@client.event
async def on_ready() :

    print("------------")
    print(" bot online")
    print("------------")
    profilo.loadUserDatabase()

client.run(TOKEN)