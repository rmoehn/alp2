from number import is_natural

def fac_iter(n):
    """
    Berechnet die Fakultät der Zahl n iterativ

    """

    # Dumme Eingaben abfangen
    if not is_natural(n):
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
    """
    Berechnet den Binomialkoeffizienten n über k über die rekursive Formel

    """

    # Dumme Eingaben abfangen
    if not is_natural(n) or not is_natural(k):
        raise Exception("n und k müssen natürliche Zahlen sein")

    # Nach Definition:
    if k > n:
        return 0

    # Rekursionsanker setzen
    if k == 0:
        return 1
    if k == 1:
        return n

    # Bühne frei für Rekursion
    return binomk_rek(n-1, k-1) + binomk_rek(n-1, k)


def binomk_iter(n, k):
    """
    Berechnet den Binomialkoeffizienten n über k iterativ

    Die Berechnung ist an die explizite Formel angelehnt. -- Sie zieht die
    Faktoren aus den Fakultäten auseinander, dividiert also erst und
    multipliziert dann.

    """

    # Dumme Eingaben abfangen
    if not is_natural(n) or not is_natural(k):
        raise Exception("n und k müssen natürliche Zahlen sein")

    # Nach Definition:
    if k > n:
        return 0

    # Binomialkoeffizienten berechnen
    res = 1
    for i in range(1, k+1):
        res *= n / i
        n -= 1  # Einfaches Dekrement ist schneller als explizite Subtraktion

    return int(res)
