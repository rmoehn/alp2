class Boolarray:
    """
    Implementiert eine Liste von Wahrheitswerten als Array von Integern

    Instead of an array of True/False (usually 8 bit each), this class creates
    an array of 8 bit-integers (does Python use 8 bit-integers?), so that
    every integer stores eigth Boolean values.

    """

    def __init__(self, tf_array=[]):
        """
        Initialise object of the Boolarray class (with some Boolean values)

        This creates the array of integers emulating an array of Boolean
        values. All indices not explicitly set are assumed to be False.

        Parameter: tf_array is an array of True/False values the new instance
        Boolarray is initialised with if given.

        """

        # Initialise the array
        self.intarray = bytearray()
            # Shouldn't be called intarray anymore. Remnants.

        # Transform given array into Boolarray
        for ind in range(len(tf_array)):
            self.set(ind, tf_array[ind])

        return


    def set(self, ind, val):
        """
        Set value at the given index in the Boolarray to True or False

        Parameters:
            ind
                Logical index of the truth value
            val
                True or False

        """

        # Calculate the physical position of the bit in the Boolarray
        real_ind   = ind // 8
        bitvec_ind = ind % 8

        # Enlarge the array if necessary
        self._expand(real_ind)

        # Set the bit
        if val == True:
            self.intarray[real_ind] |= 2**bitvec_ind

        elif val == False:
            self.intarray[real_ind] &= ~2**bitvec_ind

        else:
            raise Exception("Only True or False are accepted as val!")

        return


    def get(self, ind):
        """
        Return the value at the given index in the Boolarray

        Parameters:
            ind
                Logical index of the truth value. If it has not been accessed
                before, False is returned.

        """

        # Calculate the physical position of the bit in the Boolarray
        real_ind   = ind // 8
        bitvec_ind = ind % 8

        # Return False if array does not reach unto real_ind
        if real_ind >= len(self.intarray):
            return False

        return 0 != self.intarray[real_ind] & 2**bitvec_ind
            # Returns a Boolean value


    def len(self):
        """
        Return the logical length of the Boolarray

        The logical length is the number of bits that that are stored in the
        array.

        """

        return len(self.intarray) * 8


    def _expand(self, real_ind):
        """
        Expand integer array to the given index (fill in zeroes)

        """

        self.intarray += bytearray([0] * (real_ind - len(self.intarray) + 1))
            # Is it safe?

        return
