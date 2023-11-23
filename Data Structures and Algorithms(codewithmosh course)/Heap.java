//A heap is a complete binary tree(Parent values are greater the the children) that satisfies the heap property.
// adding [10,5,17,4,22] 
//      22
//   17     10      O(log n)--> can be proven mathematically
//4     5           removing the largest value O(log n)
public class Heap{
//leftChild =  parent*2 +1
//rightChild = parent*2 +2
//parent = (index - 1) / 2
//lastParent = (n / 2) -1
private int[] items= new int[10];
private int size;

public void insert(int value) {
    if(isFull()); 
    items[size++] = value;
    bubbleup();   
}

public int remove(){
    if(isEmpty())
     throw new IllegalStateException();

    var root = items[0];
    items[0] = items[--size];

    bubbleDown();

    return root;
}

public boolean isEmpty(){
    return size == 0;
}

private void bubbleDown(){
    var index = 0;
    while(index <= size && !isValidParent(index)){
        var largerChildIndex = largerChildIndex(index);
        swap(index, largerChildIndex);
        index = largerChildIndex;
    }
    
}

    private boolean hasLeftChild(int index) {
        return leftChildIndex(index) <= size;
    }
    private boolean hasRightChild(int index) {
        return rightChildIndex(index) <= size;
    }

    private void bubbleup(){
    var index = size - 1;
    while(index > 0 && items[index] > items[parent(index)]){
        swap(index, parent(index));
        index = parent(index);
    }
    
}

    private void swap(int first, int second) {
        var temp = items[first];
        items[first] = items[second];
        items[second] = temp;
    }

    private int parent(int index) {
        return (index-1)/ 2;
    }
    public boolean isFull(){
        return size == items.length;
    }

    private int leftChildIndex(int index) {
        return index*2 + 1;
    }

    private int rightChildIndex(int index) {

        return index*2 + 2;
    }

    private int leftChild(int index){
        return items[leftChildIndex(index)];
    }

    private int rightChild(int index){
        return items[rightChildIndex(index)];
    }

    private boolean isValidParent(int index){
        if(!hasLeftChild(index)) return true;

        var isValid = items[index] >= leftChild(index);

        if(hasRightChild(index))
             return isValid &= items[index] >= rightChild(index);

        return isValid;
    }

    private int largerChildIndex(int index){
        if(!hasLeftChild(index)) return index;

        if(!hasRightChild(index)) return leftChildIndex(index);

        return (leftChild(index) > rightChild(index)) ?
        leftChildIndex(index) : rightChildIndex(index);
        
    }

    public int max(){
        if(isEmpty()) throw new IllegalStateException();
        return items[0];
    }
    
}
