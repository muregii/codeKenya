import java.util.Arrays;

public class PriorityQueue{
    private int count;
    private int[] items = new int[5];

    public void add(int item){
        //shifting items
        //value to be inserted is for e.g 5
        //[1,4,5,6,7]
        //       6    
        if(isFull())
        throw new IllegalStateException();   
        var i = shiftItemsToInsert(item);
        items[i] = item;
        count++;
    }
    
    public boolean isFull(){
        return count == items.length;
    }
    public int shiftItemsToInsert(int item){
        int i;
        for(i = count -1; i >=0; i--){
            if(items[i] > item)

            items[i+1] = items[i];
            else
            break;
        }
        return i + 1;
    }
    
    public int remove(){
        if(isEmpty())
        throw new IllegalStateException();
        return items[--count];
    }
    
    @Override
    public String toString() {
        return Arrays.toString(items);
    }

    public boolean isEmpty(){
        return count == 0;
    }
    

}