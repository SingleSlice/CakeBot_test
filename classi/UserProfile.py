import pickle
class UserProfile : 

    cuteness = {}

    def NewUserProfile(self,discordID) : 

        ID = discordID

        if not ID in self.cuteness :

            print("new user profile")
            self.cuteness[ID] = {

                "ID discord" : ID ,
                "cuteness ammount" : 0,

            }

    def getUserProfile(self) :
        
        return self.cuteness

    def saveUserDatabase(self) :

        print("dumped")
        with open("cuteness count.pkl","wb") as d :

            pickle.dump(self.cuteness,d)
    
    def loadUserDatabase(self) :

        print("loaded")
        with open("cuteness count.pkl","rb") as d :

            self.cuteness = pickle.load(d)
        
    def addCuteness(self, ID, ammount) :
        
        print("added cuteness")
        self.cuteness[ID]["cuteness ammount"] += ammount