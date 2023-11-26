//Quick Sort Algorithm -- My Implementation

public class QuickSort{
    public void sort(int[] array){
        sort(array, 0, array.length-1 );
    }
    public void sort(int[] array, int start, int end){
        var boundary = partition(array, start, end);

        if(start >= end) return;
        sort(array, start, boundary - 1);
        sort(array, boundary + 1, end);

    }
    private int partition(int[] array, int start, int end){
        var pivot = array[end];
        var boundary = start - 1;
        // 0   2   3   7   1   4
    //                 b = index 3
         //0   2    3  1  7   4
        for(var i = start; i <= end; i++)
            if(array[i] <= pivot)
            swap(array, i, ++boundary);
            
        return boundary;    
    }
    private void swap(int[] array, int i, int j){
        int temp = array[i];
            array[i] = array[j];
            array[j] = temp;
    }
}



//chatGPT
/*public class QuickSort {
    public void sort(int[] array) {
        quickSort(array, 0, array.length - 1);
    }

    private void quickSort(int[] array, int low, int high) {
        if (low < high) {
            // pi is partitioning index, array[pi] is now at right place
            int pi = partition(array, low, high);

            // Recursively sort elements before partition and after partition
            quickSort(array, low, pi - 1);
            quickSort(array, pi + 1, high);
        }
    }

    private int partition(int[] array, int low, int high) {
        // Pivot (Element to be placed at right position)
        int pivot = array[high];  

        int i = (low - 1); // Index of smaller element

        for (int j = low; j <= high - 1; j++) {
            // If current element is smaller than the pivot
            if (array[j] < pivot) {
                i++;    // Increment index of smaller element
                swap(array, i, j);
            }
        }
        swap(array, i + 1, high);
        return (i + 1);
    }

    private void swap(int[] array, int i, int j) {
        int temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }
}
*/