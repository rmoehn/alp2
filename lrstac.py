from sorting import qsort

# Zu viele Aufgaben führen zu Plagiaten.

def generate_suffixes(A):
    """ Find all suffixes of the String A """
        # Wir plagiieren sogar orthographische Fehler mit.
        # (Miesen Programmierstil sowieso.)

    # Diese Funktion ist sogar noch ein bisschen anders.
    A = reverse_string(A)

    n = len(A)
    suffixes = []

    for i in range(n):
        if A[i:i+3] == 'CAT':
            suffixes.append(A[i:n])

    return suffixes

def find_longest_seq(B):
    max = 0
    seq = ''
    for i in range(len(B)-1):
        count = 0
        for j in range(min(len(B[i]),len(B[i+1]))):
            # Schonmal was von Gliederung gehört?
            if B[i][j]==B[i+1][j]:
                count += 1
            else:
                break
            if count > max:
                max = count
                seq = B[i][:j]
    return seq

def LRS_Algorithmus(A):
    B = generate_suffixes(A)
    B = qsort(B) # ACHTUNG: Hier ist etwas anders.
    seq = find_longest_seq(B)
    return reverse_string(seq)


# Jetzt kommt zur Abwechslung etwas eigenes

def reverse_string(string):
    """
    Dreht einen String um

    """

    out_string = ""

    for char in reversed(list(string)):
        out_string += char # rather inefficient

    return out_string

testsequence = "AAGAGCAGTGCCTCCTTTGGTGAAGGTGACACATCATGTGACCTCTTCAGTGACCACTCTACGGTGT CGGGCCTTGAACTACTACCCCCAGAAAGAGCAGACATCACCATGAAGTAAGAGCAGGGCTGAAGGA TAAGCAGCCAATGGATGCACAAGGAGTTCGAACCTAAAGACGTATTGCCCAATGGGGATGGGACCT ACCAGGGCTGGATAAAGAGCAGACCTTGGCTGTACCCCCTGGGGAAGAGCAGAGATATACGTACCA GGTGGAGCACCCAGGCCTGGATCAGCCCCTCATTGTGATCTGAAGAAGGG"
