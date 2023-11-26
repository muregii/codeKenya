//*************TRIAL 2  *********/

public class MergeSort{
    public void sort(int[] array){
        if(array.length < 2) return;

        int mid = array.length / 2;

        int[] left = new int[mid];
        for(var i = 0; i < left.length; i++){
            left[i] = array[i];
        }

        int[] right = new int[array.length - mid];
        for(var i = mid; i < array.length; i++){
            right[i - mid] = array[i];
        }

        sort(left);
        sort(right);

        merge(left, right, array);
    }

    private void merge(int[] left, int[] right, int[] result){
        int i = 0, j = 0, k = 0;

        while(i < left.length && j < right.length){
            if(left[i] <= right[j]){
                result[k++] = left[i++];
            }else{
                result[k++] = right[j++];
            }
        }

        while(i < left.length) {
            result[k++] = left[i++];
        }

        while(j < right.length) {
            result[k++] = right[j++];
        }
    }
}
// public class MergeSort {
//     public void mergesort(int[] array){
//         //Divide the array into half
//         if(array.length < 2) return;
        
//         int mid = array.length / 2;
//         int[] left = new int[mid];
//         int[] right = new int[array.length - mid];

//         for(int i = 0; i < mid; i++){
//             left[i] = array[i];
//         }

//         for(int i = mid; i < array.length; i++){
//             right[i - mid] = array[i];
//         }


//         //Sort each half.
//         mergesort(left);
//         mergesort(right);
       

//         //merge the results
//         merge(array, left, right);


//     }
//     private void merge(int[] array, int[] left, int[] right){
//         int i = 0, j = 0, k = 0;
//         while(i < left.length && j < right.length){
//             if(left[i] <= right[j]){
//                 array[k] = left[i++];
//             }else{
//                 array[k] = right[j++];
//             }
//             k++;
//         }

//         while( i < left.length){
//             array[k++] = left[i++];
//         }

//          while( i < right.length){
//             array[k++] = right[j++];
//         }
//     }
// }
