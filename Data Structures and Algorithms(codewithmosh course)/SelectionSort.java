public class SelectionSort {
    public void sort(int[] array){
        
        for(int i = 0; i < array.length; i++){
            var minIndex = i;

            for(var j = i; j < array.length; j++){
                if(array[j] < array[minIndex])
                minIndex = j;
            }
            swap(array, minIndex, i);
        }

        }

        private void swap(int[] array, int i, int j){
            int temp = array[i];
                array[i] = array[j];
                array[j] = temp;
        }

        
    }

