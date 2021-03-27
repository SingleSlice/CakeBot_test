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

    def selfHeadpatGifs(self,gif) :

        gGif = gif

        messaggio = "pat pat " + self.username
        embed = discord.Embed(title = messaggio )
        embed.set_image(url = gGif)
        
        return embed

    def otherHeadpatGifs(self,gif,mention) :

        gGif =gif

        messaggio = self.username + " caresses " + mention + "'s head"
        embed = discord.Embed(title = messaggio)
        embed.set_image(url = gGif )
        
        return embed
    
    def infoEmbed(self) : 

        messaggio = "Welcome " + self.username + " to the help section of CakeBot"
        embed = discord.Embed(title = messaggio )
        embed.add_field(name="CakeBot Hello", value="CakeBot will greet you :3", inline = False)
        embed.add_field(name = "Cakebot Omnom someone", value = "CakeBot will omnom a random person", inline = False)
        embed.add_field(name = "thanks to the friends who helped me testing and building this bot", value = "thanks Makefile_dot_in , Fabetsol , Cookie , BlueSouls ")

        return embed