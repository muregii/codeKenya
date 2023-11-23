public class PriorityQueueWithHeap{
    private Heap heap = new Heap();


    public void enqueue(int item) {
        heap.insert(item);
    }

    public int dequeue() {
        return heap.remove();
    }

    public boolean isEmpty(){
        return heap.isEmpty();
    }
}