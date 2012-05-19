from heap import Heap
import number

class PriorityQueue(Heap):
    """
    Implementiert eine Prozesswarteschlange als binärer Min-Heap

    Der Heap wird in einem eindimensialen Array gespeichert. (Eigentlich
    sollte man den Heap separat implementieren.)

    (Ich werde nicht die Funktionsnamen aus dem Aufgabenblatt übernehmen.
     Ziehe mir dafür Punkte ab, wer will.)

    """

    def is_empty(self):
        """
        Check whether the priority queue is empty

        """

        return len(self.heap) == 1


    def push(self, job):
        """
        Add a job to the queueu

        A job is a tuple (description, priority), where priority is a number
        between 1 (highest) and 100 (lowest).

        """

        # Add the job to the queue
        Heap.push(self, job)

        return


    def _check(self, job):
        """
        Check whether input tuple is valid job

        """

        priority = job[1]
        if not (number.is_natural(priority) and 1 <= priority <= 100):
            raise Exception("Priority must be natural number between 1 and "
                            + " 100")

        return


    def _compare(self, pos1, pos2):
        """
        Compare priority parts of the tuples

        """

        return self._sub_compare(self.heap[pos1][1], self.heap[pos2][1])

