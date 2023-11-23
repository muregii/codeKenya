public class MaxHeap{
    public static void heapify(int[] array){
        var lastParentIndex = array.length / 2 - 1 ;
        for (var i =  lastParentIndex; i >= 0; i--)
        heapify(array, i);
    }

    private static void heapify(int[] array, int index){
        var largerIndex = index;

        var leftIndex =  index*2 + 1;
        if(leftIndex < array.length && 
            array[leftIndex] > array[largerIndex])

        largerIndex = leftIndex;

        var rightIndex = index*2 + 2;
        if(rightIndex < array.length && array[rightIndex] > largerIndex) 
        largerIndex = rightIndex;

        if(index == largerIndex)
        return;

        swap(array, index, largerIndex);
        heapify(array, largerIndex);

    }

    private static void swap(int[] array, int first, int second){
        var temp = array[first];
        array[first] = array[second];
        array[second] = temp;
    }

    public static int getKthLargest(int[] array, int k){

        if(k < 1 || k > array.length)
        throw new IllegalArgumentException();
        
        var heap = new Heap();
        for(var number : array)
        heap.insert(number);

        for(var i = 0; i < k - 1; i++)
            heap.remove();

            return heap.max();

        }
    }
        
    
