from heap import Heap
import number
from random import seed, randrange, randint, random, choice
from sys import argv

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



def gen_random_job ():
    """
    Creates a job with random description and priority

    """

    return (randint(1000, 9999), randint(1, 100))

def random_push (queue):
    """
    Add a random job to a queue and comment

    """

    random_job = gen_random_job()
    print("Pushing this job onto the queue:", random_job)
    queue.push(random_job)
    print("Queue looks like that now:\n\t", queue.heap)

    return


def random_pop (queue):
    """
    Pop a job from a queue and comment

    """

    job = queue.pop()
    print("Popping job from queue. Got this:", job)
    print("Queue looks like that now:\n\t", queue.heap)

    return job


def random_check (queue):
    """
    Check whether queue is empty and comment

    """

    print("Checking whether queue is empty:", queue.is_empty())
    print("Queue looks like that now:\n\t", queue.heap)

    return


# Bei Aufruf als Programm Testlauf mit zufälligen Aktionen machen
if __name__ == "__main__":
    # Initialise random number generator
    if len(argv) == 2:
        seed(argv[1])
    else:
        seed()

    # Initialise priority queue with some random values
    queue = PriorityQueue(
                [gen_random_job() for i in range(randrange(10, 20))])
    print("Start queue:", queue.heap)

    # Randomly perform random actions on the queue
    for action_nr in range(0, randint(50, 100)):
        choice([random_push, random_push, random_push, random_pop, random_pop,
            random_pop, random_check])(queue)

        print()

    # Pop all that is left from the queue
    former_job = queue.heap[1]
    while former_job != None:
        cur_job = random_pop(queue)

        # Indicate problem if former job's priority was lower than the current
        if cur_job != None and former_job[1] > cur_job[1]:
            raise Exception("Detected misbehaviour: Priority of previously"
                            + " popped job was lower than the current one's.")

        former_job = cur_job

    # Last check for emptiness
    random_check(queue)

