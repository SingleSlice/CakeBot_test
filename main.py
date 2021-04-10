import discord
from classi.Keywords import Keywords
from classi.Gif import Gif
from classi.Easteregg import Eastereggs
from classi.Embedd import Embedd
from classi.UserProfile import UserProfile

intents = discord.Intents.default()
intents .members = True

TOKEN = 'ODI0MjQ5MjU3ODQyMDQ5MDI0.YFsn8A.OYXFJaWDeV4VJeW6LRFkVSWrBrs'

client = discord.Client(intents = intents)
Parole = Keywords()
gifs = Gif()
embed=discord.Embed()
embedd = Embedd()
profilo = UserProfile()

@client.event

async def on_message(message):

    if message.author.bot: return

    print("[Ti è arrivato un messaggio " + "   " + message.guild.name + "]" )   

    for parola in Parole.getKeywords() : 

        if message.content.startswith(parola) :

            if parola == Parole.Parole[1] : #CakeBot Hello

                await message.channel.send(Parole.Hello())

            elif parola == Parole.Parole[0] : #CakeBot send me a cute gif
         
                embed.set_image(url = gifs.getRandGif())
                await message.channel.send(embed=embed)
            
            elif parola == Parole.Parole[2] : #CakeBot omnom

                try :

                    message.mentions[0].name 

                except :

                    await message.channel.send("need to mention someone")
                
                else :  

                    embedd.setUserName(message.author.name)
                    await message.channel.send(embed = embedd.getOmnomGifs(gifs.getRandGifOmnom(), message.mentions[0].name))

            
            elif parola == Parole.Parole[3] : #CakeBot nice to meet you

                await message.channel.send("Hewooo , nice to meet you , im CakeBot an useless bot who can send cute gifs uwu")

            elif parola == Parole.Parole[4] : #CakeBot may i get headpats?

                embedd.setUserName(message.author.name)
                await message.channel.send(embed = embedd.selfHeadpatGifs(gifs.getRandGifHeadpat()))

            elif parola == Parole.Parole[5] : #CakeBot please headpat

                try : #try something
                    message.mentions[0].name

                except :#if there is an error (if there is no mention)
                        
                    await message.channel.send("mention someone please")

                else :

                    embedd.setUserName(message.author.name)
                    menzione = message.mentions[0].name
                    await message.channel.send(embed = embedd.otherHeadpatGifs( gifs.getRandGifHeadpat(), menzione )) #i dont even know whats going on here

            elif parola == Parole.Parole[6] : #CakeBot help
                
                embedd.setUserName(message.author.name)
                await message.channel.send(embed = embedd.infoEmbed())
            
            elif parola == Parole.Parole[7] : #CakeBot give a ticket for horny jail to

                try : #try something
                    message.mentions[0].name
                
                except :#if there is an error (if there is no mention)
                    await message.channel.send("mention someone please")

                else :
                    embedd.setUserName(message.author.name)
                    await message.channel.send(embed = embedd.getHornyJail(gifs.getHornyJailPics(), message.mentions[0].name))
            
            elif parola == Parole.Parole[8] : #CakeBot list my profile

                print("profile request")
                profilo.saveUserDatabase()
                print(profilo.getUserProfile())
                profilo.NewUserProfile(message.author.id)

@client.event

async def  on_member_join(member) :

    embedd.setGuildName(member.guild.name)
    embedd.setUserName(member.name)
    print(embedd.getUserName())
    await member.send(embed = embedd.welcomeMessage(gifs.getRandGifBenvenuto()))
    profilo.saveUserDatabase()


@client.event
async def on_ready():
    print('Logged in as :')
    print(client.user.name)
    print(client.user.id)
    print('------')
    profilo.loadUserDatabase()

    await client.change_presence(activity=discord.Game(name='type "CakeBot help" for help '))

client.run(TOKEN)

#await message.channel.send(file=discord.File('prova.txt')) mandare file