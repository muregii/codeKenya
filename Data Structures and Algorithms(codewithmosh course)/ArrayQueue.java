import java.util.Arrays;

public class ArrayQueue{
   private int[] items;
   private int rear;
   private int front;
   private int count;

   public ArrayQueue(int capacity) {
    items = new int[capacity];
   }

//enqueue
public void enqueue(int item){ 
    if(count == items.length)
    throw new IllegalStateException();
        items[rear] = item;
        rear = (rear + 1) % items.length;
        count++;
}

//dequeue
public int dequeue(){
   var  item = items[front];
    items[front] = 0;
    front = (front + 1) % items.length;
    count--;
    return item;

}
//peek
public int peek() {
    if(count == 0)
    throw new IllegalArgumentException();

    return items[count + 1 - items.length];
}

//isEmpty
public boolean isEmpty(){
    return count == 0;
}
//isFull

//toString override
@Override
public String toString(){
    var contentsonly = Arrays.copyOfRange(items,0,count);
    return Arrays.toString(contentsonly);
}
}