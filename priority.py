class PriorityQueue:
    """
    Implementiert eine Prozesswarteschlange als binärer Min-Heap

    Der Heap wird in einem eindimensialen Array gespeichert. (Eigentlich
    sollte man den Heap separat implementieren.)

    (Ich werde nicht die Funktionsnamen aus dem Aufgabenblatt übernehmen.
     Ziehe mir dafür Punkte ab, wer will.)

    """

    def __init__(self, process_list):
        """
        Initialise new PriorityQueue object with processes

        Parameters:
            process_list
                ... List of tuples of the form (description, priority)
                    representing processes. The priority is a number between 1
                    and 100, where 1 means highest priority.
        Returns:
            PriorityQueue object

        """

        # Construct a heap from the given list of processes
        self.queue = [len(process_list)] + process_list
        self._heapify()

        return


    def _heapify(self, start_pos=1):
        """
        Reorder the process queue to establish heap structure

        Parameters:
            self
                The object
            start_pos
                The array position where the reordering is started

        """


    def _left
