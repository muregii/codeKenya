import java.util.Arrays;
import java.util.Random;

public class DIYSort {
    public static void main(String[] args) {
        int N = 10000;
        int[] elements = new int[N];
        Random rng = new Random(201);
        for (int i=0; i<N; i++) { elements[i] = rng.nextInt(N); }

        //demo(elements);
        benchmark(elements);
    }

    public static void demo(int[] elements) {
        System.out.println(Arrays.toString(elements));

        // Choose your sort
        selectSort(elements);
        //insertSort(elements);
        //mergeSort(elements);

        System.out.println(Arrays.toString(elements));
    }

    public static void selectSort(int[] ar) {
        for (int i=0; i<ar.length; i++) {
            int minDex = i;
            for (int j=i+1; j<ar.length; j++) {
                if (ar[j] < ar[minDex]) {
                    minDex = j;
                }
            } 
            int temp = ar[i];
            ar[i] = ar[minDex];
            ar[minDex] = temp;
        }
    }


    public static void insertSort(int[] ar) {
        for (int i=1; i<ar.length; i++) {
            int j=i;
            while (j > 0 && ar[j-1] > ar[j]) {
                int temp = ar[j];
                ar[j] = ar[j-1];
                ar[j-1] = temp;
                j--;
            }
        }
    }

    public static void mergeSort(int[] ar) {
        mergeHelper(ar, 0, ar.length);
    }

    public static void mergeHelper(int[] ar, int l, int r) {
        int diff = r-l;
        if (diff < 2) { return; }
        int mid = l + diff/2;
        mergeHelper(ar, l, mid);
        mergeHelper(ar, mid, r);
        merge(ar, l, mid, r);
    }

    public static void merge(int[] ar, int l, int mid, int r) {
        int[] sorted = new int[r-l];
        int sDex=0; int lDex=l; int rDex=mid;
        while (lDex < mid && rDex < r) {
            if (ar[lDex] <= ar[rDex]) { 
                sorted[sDex] = ar[lDex]; 
                lDex++;
            }
            else { 
                sorted[sDex] = ar[rDex]; 
                rDex++; 
            }
            sDex++;
        }
        if (lDex == mid) { System.arraycopy(ar, rDex, sorted, sDex, r-rDex); }
        else { System.arraycopy(ar, lDex, sorted, sDex, mid-lDex); }
        System.arraycopy(sorted, 0, ar, l, r-l);
    }

    
    public static void benchmark(int[] elements) {
        int N = elements.length;
        System.out.printf("\nVarious sort timings in milliseconds");
        System.out.printf("\nN (thousands)\tselectSort\tinsertSort\tmergeSort\tjava.util sort\n");
        for (int i=0; i<4; i++) {
            System.out.printf("%d\t\t", N/1000);

            int[] copy = Arrays.copyOf(elements, N);
            long before = System.nanoTime();
            selectSort(copy);
            long after = System.nanoTime();
            System.out.printf("%d\t\t", (after-before)/1000000);
            
            copy = Arrays.copyOf(elements, N);
            before = System.nanoTime();
            insertSort(copy);
            after = System.nanoTime();
            System.out.printf("%d\t\t", (after-before)/1000000);

            copy = Arrays.copyOf(elements, N);
            before = System.nanoTime();
            mergeSort(copy);
            after = System.nanoTime();
            System.out.printf("%d\t\t", (after-before)/1000000);

            copy = Arrays.copyOf(elements, N);
            before = System.nanoTime();
            Arrays.sort(copy);
            after = System.nanoTime();
            System.out.printf("%d\t\t", (after-before)/1000000);

            System.out.printf("\n");
            int[] expanded = new int[3*N];
            System.arraycopy(elements, 0, expanded, 0, N);
            System.arraycopy(elements, 0, expanded, N, N);
            System.arraycopy(elements, 0, expanded, 2*N, N);
            elements = expanded;
            N *= 3;
        }
    }

    
}