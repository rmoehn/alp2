def longest_oneses_seq_in(bitvec):
    """
    Ermittelt Offset und Länge der längsten Folge von 1en in einem Bitvektor

    Rückgabe:
        - nichts, falls keine Einsen vorhanden
        - (offset, laenge) sonst

    Falls es mehrere längste Folgen von Einsen gibt, wird der Offset der
    ersten zurückgegeben.

    """

    # Initialise offset and length of currently examined sequence
    cur_offset = 0
    cur_length = 0

    # Initialise offset and length of longest sequence by now
    offset = 0
    length = 0

    # Initialise the former bit to 0 (important)
    former_bit = 0

    # Bitvektor Bit für Bit durchlaufen
    for bit in bitvec:
#        print("Bit:", bit)
#        print("Offset:", cur_offset)
#        print("Länge:", length)
        # On discover of a 1...
        if bit == 1:
            # Increment length of current sequence of oneses
            cur_length += 1

        # At the end of a sequence of oneses
        elif bit == 0 and former_bit == 1:
            # If it was a new longest sequence...
            if cur_length > length:
                # Update offset and length of longest sequence by now
                offset = cur_offset
                length = cur_length

            # Reset current length
            cur_length = 0

        # Do nothing on ordinary 0...
        elif bit == 0:
            pass

        # If we got neither 0 nor 1...
        else:
            raise Exception("Invalid input: A bitvector must contain naught"
                            + " but zeroeses and oneses.")

        # Set current bit as new former bit
        former_bit = bit

        # Set offset to offset of next bit
        cur_offset += 1

    # Falls keine Einsen gefunden wurden...
    if length == 0:
        # Nichts zurückgeben
        return
    # Ansonsten gewünschte Rückgabe
    else:
        return (offset - length, length)
            # offset is the offset of the end of the longest sequences of
            # oneses, thus it needs to be increased by the length of the
            # sequence.
