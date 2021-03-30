import discord

class Embedd :

    client = discord.Client()
    userID = 0
    username = ""
    guildName = ""

    def setUserName(self,name) :

        self.username = name

    def getUserName(self) :

        return self.username

    def setGuildName(self,guild) :

        self.guildName = guild

    def getGuildName(self) :

        return self.guildName

    def welcomeMessage(self,gif) :

        Ggif = gif

        messaggio = "Welcome " + self.username + " in " + self.guildName

        benvenuto = discord.Embed(title = messaggio )
        benvenuto.set_image(url = Ggif)

        return benvenuto

    def getOmnomGifs(self,gif,mention) :

        messaggio = self.username + " omnoms " + mention
        embed = discord.Embed( title = messaggio )
        embed.set_image(url = gif )

        return embed

    def selfHeadpatGifs(self,gif) :

        gGif = gif

        messaggio = "pat pat " + self.username
        embed = discord.Embed(title = messaggio )
        embed.set_image(url = gGif)
        
        return embed

    def otherHeadpatGifs(self,gif,mention) :

        gGif =gif

        if mention != "" :

            messaggio = self.username + " caresses " + mention + "'s head"
            embed = discord.Embed(title = messaggio)
            embed.set_image(url = gGif )
        
        return embed

    def getHornyJail(self, pics,mention) :

        messaggio = self.username + " sent " + mention + " to horny jail "
        embed = discord.Embed(title = messaggio)
        embed.set_image(url = pics)

        return embed


    def infoEmbed(self) : 

        messaggio = "Welcome " + self.username + " to the help section of CakeBot"
        embed = discord.Embed(title = messaggio )
        embed.add_field(name="CakeBot Hello", value="CakeBot will greet you :3", inline = False)
        embed.add_field(name = "Cakebot Omnom someone", value = "CakeBot will omnom a random person", inline = False)
        embed.add_field(name = "CakeBot nice to meet you", value = "CakeBot will be nice to meet you", inline = False)
        embed.add_field(name = "CakeBot send me a cute gif", value = "CakeBot will send a cute random gif", inline = False)
        embed.add_field(name = "CakeBot may i get headpats?", value = "CakeBot will send an headpat gif for yourself", inline = False)
        embed.add_field(name = "CakeBot please headpat", value = "CakeBot will send an headpat gif , but only if you mention someone", inline = False)
        embed.add_field(name = "CakeBot omnom", value = "CakeBot will send an omnom gif to the user you mentioned", inline = False )
        embed.add_field(name = "CakeBot give a ticket for horny jail to", value = "CakeBot will send a random 'horny jail ticket' to the user you mentioned")
        embed.add_field(name = "CakeBot help", value = "CakeBot will send this message", inline = False)
        embed.add_field(name = "thanks to the friends who helped me testing and building this bot", value = "thanks Makefile_dot_in , Fabetsol , Cookie , BlueSouls ")

        return embed
