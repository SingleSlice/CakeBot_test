import discord
from classi.Keywords import Keywords
from classi.Gif import Gif
from classi.Easteregg import Eastereggs
from classi.Embedd import Embedd

intents = discord.Intents.default()
intents.members = True

TOKEN = 'ODI0MjQ5MjU3ODQyMDQ5MDI0.YFsn8A.OYXFJaWDeV4VJeW6LRFkVSWrBrs'

client = discord.Client(intents = intents)
Parole = Keywords()
gifs = Gif()
embed=discord.Embed()
embedd = Embedd()

@client.event

async def on_message(message):

    if message.author == client.user:
        return

    print("[Ti è arrivato un messaggio]")   

    for parola in Parole.getKeywords() : 

        if message.content.startswith(parola) :

            if parola == Parole.Parole[1] : #CakeBot Hello

                await message.channel.send(Parole.Hello())

            elif parola == Parole.Parole[0] : #CakeBot send me a cute gif
         
                embed.set_image(url = gifs.getRandGif())
                await message.channel.send(embed=embed)
            
            elif parola == Parole.Parole[2] : #Cakebot Omnom someone

                await message.channel.send('Omnom')
            
            elif parola == Parole.Parole[3] : #CakeBot nice to meet you

                await message.channel.send("Hewooo , nice to meet you , im CakeBot an useless bot who can send cute gifs uwu")

            elif parola == Parole.Parole[4] : #CakeBot may i get headpats?

                embedd.setUserName(message.author.name)
                await message.channel.send(embed = embedd.selfHeadpatGifs(gifs.getRandGifHeadpat()))


@client.event

async def  on_member_join(member) :

    embedd.setGuildName(member.guild.name)
    embedd.setUserName(member.name)
    print(embedd.getUserName())
    await member.send(embed = embedd.welcomeMessage(gifs.getRandGifBenvenuto()))


@client.event
async def on_ready():
    print('Logged in as :')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)

#await message.channel.send(file=discord.File('prova.txt')) mandare file