#!/usr/bin/env python3.2
""" Einige Messungen der Ausführungszeit für die binomk-Funktionen """

from timeit import timeit
    # Das Rad neu zu erfinden ist mir zu blöd.

# Tabellenkopf ausgeben
print(" {:>2s} {:>2s} | {:>13s} | {:>13s} | {:>13s} ".format(
         "n",   "k",   "naiv", "rekursiv", "iterativ"))
print("       | {:>6s} {:>6s} | {:>6s} {:>6s} | {:>6s} {:>6s} ".format(
                 "abs/s", "rel/%", "abs/s", "rel/%", "abs/s", "rel/%"))
print("-------+---------------+---------------+---------------")

# Anzahl der Ausführungen
exec_nr = 1000

# Ausführungszeiten der naiven, rekursiven und iterativen Bino-Funktion mit
# verschiedenen ns und ks stoppen
for n in [0, 1, 3, 5, 8, 13]:
    for k in range(n+1):
        # Ausführungszeiten der verschiedenen Methoden bestimmen
        naiv_time = timeit("binomk_naiv({}, {})".format(n, k),
                           "from binomk import binomk_naiv", number=exec_nr)
        rek_time  = timeit("binomk_rek({}, {})".format(n, k),
                           "from binomk import binomk_rek", number=exec_nr)
        iter_time = timeit("binomk_iter({}, {})".format(n, k),
                           "from binomk import binomk_iter", number=exec_nr)

        # Funktion zur Berechnung der prozentualen Anteile
        tot_time  = naiv_time + rek_time + iter_time
        def rel_time(abs_time):
            return 100 * abs_time/tot_time

        # Ermittelte Zeiten spaltenweise ausgeben
        print(" {:>2d} {:>2d} | {: >6.3f} {: >6.3f}".format(
                n,     k,     naiv_time, rel_time(naiv_time)),
              "| {: >6.3f} {: >6.3f} | {: >6.3f} {: >6.3f} ".format(
                rek_time, rel_time(rek_time), iter_time, rel_time(iter_time))
        )

    # Leerzeile zwischen den verschiedenen ns ausgeben
    print()
