import random

class MontyHallGame:
    """
    Klasse zur Simulation des Monty-Hall-Spieles

    -- besser bekannt als Drei-Türen-Spiel, Zonk (?) oder Spiel mit drei
    Türen, zwei Ziegen, einem Auto, einem Moderator, einem Spieler und sechs
    Scharnieren

    (Die meisten der folgenden Methoden sollten durch vorangehenden
     Unterstrich als privat markiert werden.)

    """

    # Set to true or false on the end of a game
    player_has_won = None

    def __init__(self):
        """
        Initialise object of the MontyHallGame class

        The object is initialised with random positions for the car and
        (implicitly) the goats behind the doors.

        """

        # Initialise the random number generator
        random.seed()

        # Set the position of the car randomly (should be private, of course)
        self.car_pos = random.randint(1, 3)

        return

    def ask_door(self):
        """
        Ask the player which door to open

        """
        self.usr_choice = int(input("Ist das Auto hinter Tür 1, 2 oder 3? "))

        return

    def rand_door(self):
        """
        Automatically choose random door

        """
        self.usr_choice = random.randint(1, 3)

        return

    def open_door(self):
        """
        Moderator half-randomly chooses a door to open

        """

        # Exclude doors the user has chosen or with the car behind
        possible_doors = [1, 2, 3]
        possible_doors.remove(self.usr_choice)
        try: # Might have been removed already
            possible_doors.remove(self.car_pos)
        except ValueError:
            pass

        # Choose from the remaining and store
        self.opened_door = random.choice(possible_doors)

        return

    def ask_change(self):
        """
        Ask user whether he wants to change

        """
        self.usr_choice = int(input(
            "Hinter Tür {0} ist eine Ziege.".format(self.opened_door)
            + " Wollen Sie bei Tür {0} bleiben".format(self.usr_choice)
            + " oder nicht doch lieber die andere Tür nehmen? "
        ))

        return

    def rand_change(self):
        """
        Automatically choose one of the two closed doors

        This may be the former choice or the other one.

        """

        # Set doors to choose from
        possible_doors = [1, 2, 3]
        possible_doors.remove(self.opened_door)

        # Choose one of the closed doors
        self.usr_choice = random.choice(possible_doors)

        return

    def change_door(self):
        """
        Choose the formerly not chosen door for opening

        """

        # Determine door that was neither opened nor chosen before
        possible_doors = [1, 2, 3]
        possible_doors.remove(self.opened_door)
        possible_doors.remove(self.usr_choice)

        # Choose it
        self.usr_choice = possible_doors[0]

        return

    def evaluate(self):
        """
        See whether player has won or not

        """

        # Dummheiten des Benutzers abfangen
        if self.usr_choice == self.opened_door:
            raise Exception("Spieler hat die schon geöffnete Tür gewählt."
                            + " Das ist idiotisch.")

        # Hat er nun gewonnen?
        if self.usr_choice == self.car_pos:
            self.player_has_won = True
            return 1 # Return numbers as counting aid in massive simulation
        else:
            self.player_has_won = False
            return 0

    def gratulate(self):
        """
        Tell the player her doom

        """
        if self.player_has_won == True:
            print("Gratulation, Sie haben ein Auto gewonnen!")
        else:
            print("Mehehe.")

        return

    def play_interactively(self):
        """
        Führt ein interaktives Spiel mit hübschen Eingabeaufforderungen durch

        """

        # Avoid the fallacy of playing the same object twice
        if self.player_has_won in {True, False}:
            raise Exception("Dieses Spiel ist schon gespielt worden!")

        # Conduct a game
        self.ask_door()
        self.open_door()
        self.ask_change()
        self.evaluate()
        self.gratulate()

        return

    def play_automatically(self, change="random", verbose=False):
        """
        Führt ein Spiel automatisch und zufällig durch

        Parameter ``change`` legt die Strategie des Spielers fest: Bei
        "always" wird die Tür immer gewechselt, nachdem der Moderator eine
        geöffnet hat, bei "never" nie und bei "random" wird zufällig
        entschieden, ob gewechselt wird oder nicht.

        Falls ``verbose`` True ist, werden die erst gewählte Tür, die vom
        Moderator geöffnete Tür, die dann gewählte Tür und das Ergebnis
        ausgegeben.

        """

        # Avoid the fallacy of playing the same object twice
        if self.player_has_won in {True, False}:
            raise Exception("Dieses Spiel ist schon gespielt worden!")

        # Conduct an automatic game
        self.rand_door()
        if verbose:
            print("gewählte Tür:", self.usr_choice)

        self.open_door()

        # Türwechsel auf Basis der angegebenen Strategie
        if change == "random":
            self.rand_change()
        elif change == "always":
            self.change_door()
        elif change == "never":
            pass
        else:
            raise Exception("Third parameter must be one of 'random',"
                            + " 'always' or 'never'")

        if verbose:
            print("geöffnete Tür:", self.opened_door)
            print("nun gewählte Tür:", self.usr_choice)
            print("Autotür:", self.car_pos)
            print()

        return self.evaluate()

    def simulate(times, change="random"):
        """
        Simulate ``times`` rounds of the game

        ``change`` as above.

        """

        # Initialise Number of won games
        won_cnt = 0

        # Conduct the games
        for cnt in range(times):
            game = MontyHallGame()
            won_cnt += game.play_automatically(change)

        return won_cnt


# Bei Aufruf als Programm, soll der Benutzer spielen
if __name__ == "__main__":
    game = MontyHallGame()
    game.play_interactively()
