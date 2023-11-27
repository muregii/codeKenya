public class Search {
    //LINEAR SEARCH
   public int LinearSearch(int[] array, int target){

    for(int i = 0; i < array.length; i++){
        if(array[i] == target){
            return i;
        }
        
    }
    return -1;
    
} 
//BINARY SEARCH
public int binarySearch(int[] array, int target){ //O(log n)

    var left = 0;
    var right = array.length - 1;

    while(left <= right){
        var middle = left + (right - left) / 2; // OR var middle = (left + right) / 2;

        if(array[middle] == target) return middle;

        if(target < array[middle])
            right = middle - 1;
        else
            left = middle + 1;

    }
    return -1;
}

 //O(log(3) n)  TERNARY SEARCH
    public int ternarySearch(int[] array, int target){
        return ternarySearchRec(array, target, 0, array.length - 1);
    }
    
        private int ternarySearchRec(int[] array, int target, int left, int right){
            //our partition size = (right - left) / 3;
            if(right >= left){
                var mid1 = left + (right - left) / 3;
                var mid2 = right - (right - left) / 3;
                
                
                if(array[mid1] == target)
                    return mid1;
                
                if(array[mid2] == target)
                    return mid2;
                
                if(target < array[mid1]){
                    return ternarySearchRec(array, target, left, mid1 - 1);

                }else if(target > array[mid2]){

                    return ternarySearchRec(array, target, mid2 + 1, right);
                }else{

                    return ternarySearchRec(array, target, mid1 + 1, mid2 - 1);
                }

            }
            return -1;
                

    }

    //O(Sq(n))
    public int jumpearch(int[] array, int target){
        var start = 0;
        var next = 0;
        
    }
}




