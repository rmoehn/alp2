COINS = (200, 100, 50, 20, 10, 5, 2, 1)

def change_money_rec(amount, coins=COINS):
    """
    Berechnet die günstigste Kombination von Münzen für einen Geldbetrag

    - rekursive Variante

    Parameter:
        - amount ... Geldbetrag in Euros.Cents
        - coins  ... Liste der möglichen Münzen in Centäquivalent von groß
                     nach klein
    Rückgabe:
        Liste der den Geldbetrag bildenden Münzen in Centäquivalent

    """

    def cmr_helper(amount, coins):
        """ Helper function doing the actual recursion. Same parameters. """
        # If there is no money left to be divided into coins...
        if amount == 0:
            return []

        # If remaining amount of money is too small to be expressed in coins
        if coins == [] and amount > 0:
            # ...die.
            raise Exception("Restbetrag kleiner als die kleinste Münze!")

        # If currently biggest coin fits into the amount of money...
        if coins[0] <= amount:
            # Put the coin into the list of returned coins and proceed with
            # the remaining money
            return [ coins[0] ] + cmr_helper( amount - coins[0], coins )

        # If currently biggest coin does not fit into the amount of money...
        if coins[0] > amount:
            # Remove the biggest coin from the list of available coins
            coins.pop(0)

            # Proceed with the old amount of money and the new set of coins
            return cmr_helper(amount, coins)

    # Convert amount of money into cents
    amount *= 100

    # Prohibit non-integer cents
    if amount != int(amount):
        raise Exception("Gebrochene Cents sind nicht erlaubt.")

    # Call helper function with now appropriate money format
    return cmr_helper(amount, list(coins))


def change_money_iter(amount, coins=COINS):
    """
    Berechnet die günstigste Kombination von Münzen für einen Geldbetrag

    - iterative Variante

    Parameter:
        - amount ... Geldbetrag in Euros.Cents
        - coins  ... Liste der möglichen Münzen in Centäquivalent von groß
                     nach klein
    Rückgabe:
        Liste der den Geldbetrag bildenden Münzen in Centäquivalent

    """

    # Convert amount of money into cents
    amount *= 100

    # Prohibit non-integer cents
    if amount != int(amount):
        raise Exception("Gebrochene Cents sind nicht erlaubt.")

    # Make a copy of the input list (tuple) of coins for use here
    rem_coins = list(coins)

    # Initialise list of returned coins
    change = []

    # Go on until the whole amount of money has been divided up into coins
    while amount > 0:
        # If remaining amount of money is too small to be expressed in coins
        if rem_coins == []:
            # ...die (or not).
            raise Exception("Restbetrag kleiner als die kleinste Münze!")

        # If currently biggest coin fits into the amount of money...
        if rem_coins[0] <= amount:
            # Put the coin into the list of returned coins and proceed with
            # the remaining money
            change += [ rem_coins[0] ]
            amount -= rem_coins[0]

        # Currently biggest coin does not fit into the amount of money.
        else:
            # Proceed removing it from the list of available coins
            rem_coins.pop(0)

    return change
