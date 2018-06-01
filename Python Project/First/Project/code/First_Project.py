class project():
    
    def showdetails(self,name):
        players = input(name +" enter the no.")
        if (name == "player1"):
             print("a")
        else:
            print("b")
      
            
def main(): 
    num = project()
    num.showdetails("player1")
    num.showdetails("player2")
    
     
if __name__=="__main__":
     main()