import pickle
class UserProfile : 

    profili = {}

    def NewUserProfile(self,discordID) : 

        

        ID = discordID

        if not ID in self.profili :

            print("new user profile")
            self.profili[ID] = {

                "ID discord" : ID ,
                "cuteness ammount" : 0,

            }


    def getUserProfile(self) :
        
        return self.profili

    def saveUserDatabase(self) :

        print("dumped")
        with open("cuteness count.pkl","wb") as d :

            pickle.dump(self.profili,d)
    
    def loadUserDatabase(self) :

        print("loaded")
        with open("cuteness count.pkl","rb") as d :

            self.profili = pickle.load(d)
    
