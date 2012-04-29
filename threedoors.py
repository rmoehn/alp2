import random

class MontyHallGame:
    """
    Klasse zur Simulation des Monty-Hall-Spieles

    -- auch bekannt als Drei-Türen-Spiel, Zonk (?) oder Spiel mit drei Türen,
    zwei Ziegen, einem Auto, einem Moderator, einem Spieler und sechs
    Scharnieren

    """

    def __init__(self):
        """
        Return a new object of the MontyHallGame class

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

    def open_door(self):
        """
        Moderator half-randomly chooses a door to open

        """

        # Exclude doors the user has chosen and with a car behind
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

        # Benutzer fragen, ob er sich auch sicher ist
        self.usr_choice = int(input(
            "Hinter Tür {0} ist eine Ziege.".format(self.opened_door)
            + " Wollen Sie bei Tür {0} bleiben".format(self.usr_choice)
            + " oder nicht doch lieber die andere Tür nehmen? "
        ))

        return

    def evaluate(self):
        """
        See whether player has won or not

        """

        # Dummheiten des Benutzers abfangen
        if self.usr_choice == self.opened_door:
            raise Exception("Spieler hat die schon geöffnete Tür gewählt."
                            + " Das ist idiotisch.")

        if not self.usr_choice in {1, 2, 3}:
            raise Exception("Spieler hat Tür gewählt, die es gar nicht"
                            + " gibt.")

        # Hat er nun gewonnen?
        if self.usr_choice == self.car_pos:
            self.player_has_won = True
            return 1
        else:
            self.player_has_won = False
            return 0

    def gratulate(self):
        if self.player_has_won == True:
            print("Gratulation, Sie haben ein Auto gewonnen!")
        else:
            print("Mehehe.")

        return

    def play_interactively(self):
        self.ask_door()
        self.open_door()
        self.ask_change()
        self.evaluate()
        self.gratulate()

        return
