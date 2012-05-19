class Heap:
    """
    Implementiert einen generischen Heap

    Der Heap wird mit einem Array implentiert. Abgeleitete Klassen werden
    meistens die _compare-Funktion überschreiben oder erweitern. Die hier
    definierte vergleicht die Einträge des Arrays so, dass ein Min-Heap
    entsteht.

    Note: The following differentiates between 'index' and 'position'. 'index'
    is the real array index starting from 0, whereas 'position' is the
    position in the heap part of the array starting from 1.

    """

    def __init__(self, array):
        """
        Initialise heap object with array

        """

        # Set up and order internal array to form a heap
        self.heap = [len(array)] + array
        self._build_heap()

        return


    def _build_heap(self):
        """
        Rearrange elements in internal array to (re-)establish heap

        """

        # Reorder all subtrees from bottom to top, omitting leaves
        for pos in range(self._calc_size() // 2, 0, -1):
            self._heapify_subtree(pos)

        return


    def push(self, elem):
        """
        Add an element to the heap

        """

        # Insert element into internal array
        self.heap.insert(1, elem)

        # Reestablish heap structure
        self._inc_size()
        self._build_heap()

        return


    def pop(self):
        """
        Remove element from the top of the heap and return it

        """

        # Check for empty heap
        if self._calc_size() == 0:
            return None

        # Remove topmost element
        top_elem = self.heap[1]
        del self.heap[1]

        # Repair heap
        self._dec_size()
        self._build_heap()

        return top_elem


    def _heapify_subtree(self, pos):
        """
        Rearrange nodes violating the heap property

        Paramters:
            pos
                Position of the node to rearrange

        """

        # Get positions of the children
        left_pos  = self._calc_lchild_pos(pos)
        right_pos = self._calc_rchild_pos(pos)

        # Get size of the heap (upper boundary)
        heapsize  = self._calc_size()

        # Look whether left or right child should be in the current position
        if left_pos <= heapsize and self._compare(left_pos, pos) == -1:
            new_tnode_pos = left_pos
        else:
            new_tnode_pos = pos
        if right_pos <= heapsize \
            and self._compare(right_pos, new_tnode_pos) == -1:
            new_tnode_pos = right_pos

        # If the position of the element that should be in the current
        # position is not the current position
        if new_tnode_pos != pos:
            # Exchange elements
            self.heap[pos], self.heap[new_tnode_pos] = \
                self.heap[new_tnode_pos], self.heap[pos]

            # Rearrange subsequent nodes of the changed node
            self._heapify_subtree(new_tnode_pos)

        return


# Hilfs-Hilfsfunktionen
    def _calc_parent_pos(self, pos):
        """ Return position of parent node in the heap array """
        return pos // 2

    def _calc_rchild_pos(self, pos):
        """ Return position of right child node in the heap array """
        return pos *  2

    def _calc_lchild_pos(self, pos):
        """ Return position of left child node in the heap array """
        return pos * 2 + 1

    def _calc_size(self):
        """ Return size/upper boundary of the heap (not the array!) """
        return self.heap[0]

    def _inc_size(self):
        """ Increment size/upper boundary of the heap """
        self.heap[0] += 1
        return
    def _dec_size(self):
        """ Decrement size/upper boundary of the heap """
        self.heap[0] -= 1
        return

    def _compare(self, pos1, pos2):
        """
        Compare-Funktion für einen Min-Heap mit einfachen Knoten

        Return -1 if the element in pos1 is less than the element in pos2,
        1 if it is greater, 0 if they are equal.

        To be overridden by most derived classes.

        """

        if   self.heap[pos1] < self.heap[pos2]:
            return -1
        elif self.heap[pos1] > self.heap[pos2]:
            return 1
        else:
            return 0

