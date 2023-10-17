# Define the base class player
class Player:
    def play(self):
        print("The player is playing cricker.")

# Define the derived class Batsman
class Batsman (Player):
    def play(self):
        print("The batsman is batting.")
#define the derived class Bowler
class Bowler (Player):
    def play(self):
        print("The bowler is bowling.")
#create objects of Batsman and Bowler classes
batsman = Batsman()
bowler = Bowler()
 #call the  playt()  method for each object
batsman.play()
bowler.play()
        