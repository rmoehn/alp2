COINS = [200, 100, 50, 20, 10, 5, 2, 1]

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

    def cmr_helper(amount, coins=coins):
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

    # Call helper function with now appropriate money format
    return cmr_helper(amount)
