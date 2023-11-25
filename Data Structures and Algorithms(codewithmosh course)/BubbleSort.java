public class BubbleSort {
    public void sort(int[] n){
    boolean isSorted;
    
    for(int index2 = 0; index2 < n.length - 1; index2++ ){
        isSorted = true;
        for(int index1 = 0; index1 < n.length - index2 - 1; index1++)
            if(n[index1] > n[index1 + 1]){
                swap(n, index1, index2);
                isSorted = false;    
            } 
              if(isSorted) return;
    }  
}
    
    private void  swap(int[] n, int index1, int index2 ){
        int temp = n[index1];
        n[index1] = n[index1 + 1];
        n[index1 + 1] = temp;  
    }
}

