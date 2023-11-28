import java.util.NoSuchElementException;

public class LinkedList {
    private class ListNode{
        private int info;
        private ListNode next;
       
       public ListNode (int info) {
        this.info = info;
       }
        
}

private ListNode first;
private ListNode last;
private int size;

//addFirst
public void addFirst(int item) {
    var node = new ListNode(item);
    
    if (isEmpty()) 
    first = last = node;
    else{
        node.next = first;
        first = node;
    }
    size++;
}
//addLast
public void addLast(int item) {
    var node = new ListNode(item);
    if (isEmpty()) 
        first = last = node;
        else{
            last.next = node;
            last = node;
        }
    size++;
}

private boolean isEmpty() {
    return first == null;
}
//deleteFirst
public void removeFirst() {
    if(isEmpty())
    throw new NoSuchElementException();
    
    var second = first.next;
    first.next = null;
    first = second;
size--;
}
//deleteLast
public void removeLast() {
    //no nodes edge case
    if(isEmpty())
    throw new NoSuchElementException();
    //single node edge case
    if(first == last) 
        first = last = null;
        else{
            //[10 -> 20 -> 30]
        //previous points to 20 here
        var previous = getPrevious(last);
        last = previous;
        last.next = null;
        }
        size--;
    }
    
private ListNode getPrevious(ListNode node){
    var current = first;
    while (current != null){
        if(current.next == node) 
        return current;
        else{
            current = current.next;
        }
        
    }
    return null;
    }
//contains
public boolean contains(int item) {
    return indexOf(item) != -1;
}
//indexOf
public int indexOf (int item) {
    int index = 0;
    var current = first;
    while(current != null) {
        if(current.info == item) 
        return index;      
        current = current.next;
        index++;                 
    }
    return -1;
}
//size
public int size() {    
    return size;
}

public int[] toArray() {
    int[] array = new int[size];
    var current = first;
    var index = 0;

    while(current != null) {
        array[index++] = current.info;
        current = current.next;
    }
    return array;
}

public void reverse() {

    if(isEmpty()) return;
    
    var previous = first;
    var current = first.next;
    
    while(current != null) {
        var temp = current.next;
        current.next = previous;
        previous = current;
        current = temp;
    }
     
    last = first;
    last.next = null;
    first = previous;
}

public int findKthFromTheEnd(int k) {
//[10 -> 20 -> 30 -> 40 -> 50]
//              *            *
if(isEmpty()) 
throw new IllegalStateException();

var pointer1 = first;
var pointer2 = first;
for(int i = 0; i < k-1; ++i) {
    pointer2 = pointer2.next;
    if(pointer2 == null)
    throw new IllegalArgumentException();
}

while(pointer2 != last) {
    pointer1 = pointer1.next;
    pointer2 = pointer2.next;
}
return pointer1.info;


}

public void printMiddle() {

    if(isEmpty())
    throw new IllegalStateException();

    var a = first;
    var b = first;
    while(b != last && b.next != last ){
     a = a.next;
     b = b.next.next;
    }

    if(b == last) 
    System.out.println(a.info);
    else
    System.out.println(a.info + "," + a.next.info);

}
public boolean hasLoop(){
    var a = first;
    var b = first;

    while(b != last && b.next != last){
        a = a.next;
        b = b.next.next;
    }
    
    return true;
}  
   
}