class Heap:
    """
    Implementiert einen allgemeinen Heap

    """

    def __init__(self, array):
        self.heap = [len(array)] + array

        for pos in range(self._size() // 2, 0, -1):
            self._heapify(pos)

        print(self.heap)

        return

    def _heapify(self, pos):
        left_pos  = self._calc_lchild_pos(pos)
        right_pos = self._calc_rchild_pos(pos)

        heapsize  = self._size()

        if left_pos <= heapsize and self._compare(left_pos, pos) == -1:
            new_tnode_pos = left_pos
        else:
            new_tnode_pos = pos

        if right_pos <= heapsize \
            and self._compare(right_pos, new_tnode_pos) == -1:
            new_tnode_pos = right_pos

        if new_tnode_pos != pos:
            self.heap[pos], self.heap[new_tnode_pos] = \
                self.heap[new_tnode_pos], self.heap[pos]
            self._heapify(new_tnode_pos)

        return

    def _calc_parent_pos(self, pos):
        return pos // 2

    def _calc_rchild_pos(self, pos):
        return pos *  2

    def _calc_lchild_pos(self, pos):
        return pos * 2 + 1

    def _size(self):
        return self.heap[0]

    def _compare(self, pos1, pos2):
        """
        Compare-Funktion für einen Min-Heap mit einfachen Knoten

        """

        if   self.heap[pos1] < self.heap[pos2]:
            return -1
        elif self.heap[pos1] > self.heap[pos2]:
            return 1
        else:
            return 0
