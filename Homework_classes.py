class Games:
    """This is the superclass"""
    def __init__(self, name, min_age, min_num_players, max_num_players, game_duration):
        """all properties are set here as default variables"""
        self.name = name
        self.min_age = min_age
        self.min_num_players = min_num_players
        self.max_num_players = max_num_players
        self.game_duration = game_duration
        self.number_of_times_played = 0

    def __str__(self):
        return "The chosen game is called {}.".format(self.name)
    
    def play(self, num_people, expected_fun_duration, age_youngest):
        """This method checks all the properties and counts one game played if compliant"""

        if num_people < self.min_num_players:
            print("You don't have enough players for this game!")
            return False
        elif num_people > self.max_num_players:
            print("You have too many players for this game.")
            return False
        
        if expected_fun_duration < self.game_duration:
            print("{} takes on average longer than the time you have available!".format(self.name))
            return False
        
        if age_youngest < self.min_age:
            print("The youngest player is too young for {}!".format(self.name))
            return False
        
        else:
            self.number_of_times_played += 1
            print("You played {}".format(self.name), self.number_of_times_played, "times.")
            return True

class Boardgame(Games):
    """This is the first subclass"""
    def game_type(self):
        print("{} is a board game.".format(self.name))

class Cardgame(Games):
    """This is the second subclass"""
    def game_type(self):
        print("{} is a card game.".format(self.name))

class Tichu(Cardgame):
    """This is a subclass of the second subclass"""
    def play(self, num_people, expected_fun_duration, age_youngest):
        if num_people == 2:
            print("With 2 players you can play Tichu Nanjing.")
        elif num_people == 3:
            print("With 3 players you can play the version of Tichu called Trichu!")
        elif num_people == 6:
            print("With 6 players you can play Tichu Tientsin.")
        elif num_people > 4:
            print("A version of this game for 5 to 12 players is called Grandseigneur.")
        super().play(num_people, expected_fun_duration, age_youngest)

"""Here the classes and the different properties are set for each game"""
# ticket_to_ride = Boardgame("Ticket_to_ride", 8, 2, 5, 60)
# settlers_of_catan = Boardgame("Settlers_of_Catan", 10, 3, 4, 75)
# tichu = Tichu("Tichu", 10, 3, 12, 60)
# jolly = Cardgame("Jolly", 6, 2, 6, 30)
# schnapsen = Cardgame("Schnapsen", 6, 2, 4, 30)

"""Method of objects are called"""
# ticket_to_ride.play(3, 120, 9)
# ticket_to_ride.play(3, 30, 9)
# tichu.play(6, 120, 12)
# settlers_of_catan.play(4, 75, 12)
# ticket_to_ride.play(3, 120, 9)
# jolly.play(5, 60, 8)
# schnapsen.play(2, 60, 6)

"""Here, a list of games and properties is created to be able to call all the games at once"""
games = [
    Boardgame("Ticket_to_ride", 8, 2, 5, 60), 
    Boardgame("Settlers_of_Catan", 10, 3, 4, 75), 
    Tichu("Tichu", 10, 3, 12, 60), 
    Cardgame("Jolly", 6, 2, 6, 30), 
    Cardgame("Schnapsen", 6, 2, 4, 30)
    ]

"""One after the other game is called and a given set of variables is used for each of them"""
for game in games:
    print(game)
    game.game_type()
    game.play(3, 60, 9)
    