from collections import deque

def count_hanoi_steps(disc_cnt):
    """
    Führt die Sache mit den Hanoi-Türmen iterativ durch

    Parameter:
        disc_cnt
            Anzahl der Scheiben

    Rückgabe:
        Anzahl der benötigten Schritte

    """

    # Drei Stangen initialisieren. -- Zahlen entsprechen Scheiben
    pegs = {}
    pegs["quelle"] = [i for i in range(disc_cnt, 1, -1)]
    pegs["hilfe"]  = []
    pegs["ziel"]   = []

    # Queue für die Positionen der kleinsten Scheibe initialisieren
    smallest_q = None

    # Start: kleinste Scheibe auf bestimmte Stange tun
    if disc_cnt % 2 == 0:
        pegs["hilfe"].append( 1 )
        smallest_q = deque(["ziel", "quelle", "hilfe"])

    else:
        pegs["ziel"].append( 1 )
        smallest_q = deque(["hilfe", "quelle", "ziel"])

    # Leiern bis alle Scheiben auf der Zielstange und Schritte zählen
    steps = 1
    while len(pegs["ziel"]) < disc_cnt:
        # Legalen Zug machen. smallest_q[0] und smallest_q[1] sind die Stäbe,
        # wo die kleinste Scheibe nicht ist. Ist ein Stab leer, wird die
        # nicht-kleinste Scheibe dort hingetan. Ist auf beiden Stäben etwas,
        # wird die kleinere Scheibe auf die größere getan.
        if pegs[ smallest_q[0] ] == []:
            pegs[ smallest_q[0] ].append( pegs[ smallest_q[1] ].pop() )
        elif pegs[ smallest_q[1] ] == []:
            pegs[ smallest_q[1] ].append( pegs[ smallest_q[0] ].pop() )

        elif pegs[ smallest_q[1] ][-1] > pegs[ smallest_q[0] ][-1]:
            pegs[ smallest_q[1] ].append( pegs[ smallest_q[0] ].pop() )
        else:
            pegs[ smallest_q[0] ].append( pegs[ smallest_q[1] ].pop() )

        # Kleinste Scheibe dorthin verschieben, wo sie davor nicht war
        new_peg = smallest_q.popleft() # Zielstab bestimmen
        pegs[new_peg].append(1)        # Scheibe dort anhängen
        pegs[smallest_q[-1]].pop()     # vom alten Stab entfernen
        smallest_q.append(new_peg)     # als übernächsten Zielstab eintragen

        # Anzahl der Züge um 2 inkrementieren
        steps += 2

    return steps
