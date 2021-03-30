from random import *

GifNum = 7

class Gif :

    listaGif = [

        "https://media.giphy.com/media/Id0IZ49MNMzKHI9qpV/giphy.gif", #0
        "https://media.giphy.com/media/8MFkW6mDff37G/giphy.gif", #1
        "https://media.giphy.com/media/3o7bul4bNw60uhhQyI/giphy.gif", #2
        "https://media.giphy.com/media/JWGgsu82QDoEE/giphy.gif",#3
        "https://media.giphy.com/media/a6pzK009rlCak/giphy.gif",#4
        "https://media.giphy.com/media/N4AIdLd0D2A9y/giphy.gif",#5
        "https://media.giphy.com/media/10N247rib4BlVC/giphy.gif",#6
        "https://media.giphy.com/media/CNUb51EbTxuRG/giphy.gif"#7

    ]


    listaGifBenvenuto = [

        "https://media.giphy.com/media/9cZQnwdzUXTDG/giphy.gif", #0
        "https://media.giphy.com/media/yyVph7ANKftIs/giphy.gif" #1

    ]

    listaGifHeadpat = [

        "https://media.giphy.com/media/ARSp9T7wwxNcs/giphy.gif", #0
        "https://media.giphy.com/media/Z7x24IHBcmV7W/giphy.gif", #1
        "https://cdn.weeb.sh/images/HyG2kJKD-.gif", #2

    ]

    listaGifOmnom = [

        "" #0

    ]

    hornyjail = [

        "https://i.imgur.com/tJlR45p.gif" #0

    ]


    def getGifs(self) :

        return self.listaGif    
     
    def getRandGif(self) :

        GifNum = 7
        n = randint(0,GifNum)
        return self.listaGif[n]

    def getRandGifOmnom(self) :

        GifNum = 0
        n = randint(0, GifNum)
        return self.listaGifOmnom[n]

    def getRandGifBenvenuto(self) : 

        GifNum = 1
        n = randint(0,GifNum)

        return self.listaGifBenvenuto[n]

    def getRandGifHeadpat(self) :

        GifNum = 1
        n = randint(0,GifNum)

        return self.listaGifHeadpat[n]

    def getHornyJailPics(self) :

        GifNum = 0
        n= randint(0, GifNum)
    
        return self.hornyjail[n]


