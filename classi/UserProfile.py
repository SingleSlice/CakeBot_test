import pickle
class UserProfile : 

    cuteness = {}

    databasePath = "D:\\programmi\\programmi miei\\python\\SingleSliceOfRam\\cuteness count.pkl"

    def NewUserProfile(self,discordID) : 

        ID = discordID

        if not ID in self.cuteness :

            print("new user profile")
            self.cuteness[ID] = {

                "ID discord" : ID ,
                "cuteness ammount" : 0

            }
        
            self.saveUserDatabase()

    def getUserProfile(self) :
        
        return self.cuteness

    def saveUserDatabase(self) :

        print("dumped")
        with open(self.databasePath,"wb") as d :

            pickle.dump(self.cuteness,d)
    
    def loadUserDatabase(self) :

        print("loaded")
        with open(self.databasePath,"rb") as d :

            self.cuteness = pickle.load(d)
        