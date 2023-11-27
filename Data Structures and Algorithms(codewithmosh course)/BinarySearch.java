public class BinarySearch {
public int binarySearchRec(int[] array, int target){
    return binarySearchRec(array, target, 0, array.length - 1);
}

    private int binarySearchRec(int[] array, int target, int left, int right){
        if(right < left) return -1;
        
        int middle = left + (right - left) / 2; //Integer overflow for large values
        //int middle = (left + right) / 2;
        if(array[middle] == target) return middle;

        if(target < array[middle])
        return binarySearchRec(array, target, left, middle - 1);

        return binarySearchRec(array, target, middle + 1, right);
    }
}
