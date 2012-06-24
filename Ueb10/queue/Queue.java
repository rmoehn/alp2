package queue;

public interface Queue<ElemType> {
    public void enqueue(ElemType element);
    public ElemType dequeue() throws EmptyQueueException;
    public ElemType head() throws EmptyQueueException;
    public boolean empty();
    public String toString(); // Von wegen void!
}
