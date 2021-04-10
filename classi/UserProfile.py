import pickle
class UserProfile : 

    profili = {}

    def NewUserProfile(self,discordID, discordName) : 

        print("new user profile")

        ID = discordID
        nickname = discordName

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