import number

def fac_iter(n):
    """
    Berechnet die Fakultät der Zahl n iterativ

    """

    # Dumme Eingaben abfangen
    if not number.is_natural(n):
        raise Exception("Wir berechnen nur Fakultäten von natürlichen"
                        + " Zahlen. Für andere Zahlenbereiche ist die"
                        + " Gammafunktion zu verwenden.")

    # Fakultät berechnen
    factorial = 1 # 0! = 1
    for factor in range(2, n+1):
        factorial *= factor

    return factorial


def binomk_naiv(n, k):
    """
    Berechnet den Binomialkoeffizienten n über k naiv und rekursionsfrei

    Benutzt wird die Formel (n k) = n! / ((n-k)! * k!).

    """

    # Nach Definition:
    if k > n:
        return 0
    # Übrige problematische Eingaben werden von fac_iter abgefangen
    else:
        return fac_iter(n) // (fac_iter(n - k) * fac_iter(k))


def binomk_rek(n, k):
