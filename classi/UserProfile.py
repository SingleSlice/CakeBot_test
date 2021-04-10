import pickle
class UserProfile : 

    profili = {}

    def NewUserProfile(self,discordID) : 

        print("new user profile")

        ID = discordID

        if not ID in self.profili :

            self.profili[ID] = {}


    def getUserProfile(self) :
        
        return self.profili

    def saveUserDatabase(self) :

        print("dumped on the toilet")
        with open("database.pkl","wb") as d :

            pickle.dump(self.profili,d)
    
    def loadUserDatabase(self) :

        print("loaded")
        with open("database.pkl","rb") as d :

            self.profili = pickle.load(d)
    
