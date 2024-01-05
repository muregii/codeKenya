//Top 150 interview. #88
public class MergeSortedArray {
    public int[] merge(int[] a, int m,  int[] b, int n){
        var i = m-1;
        var j = n-1;
        var last = m+n-1;

        while(i >= 0 && j >= 0){
            /*Input: nums1 = [1,2,2,3,5,6], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6] */
            if(a[i] > b[j]){
                a[last] = a[i];
                i--;
            }else{
                a[last] = b[j];
                j--;
            }
            last--;

        }

        while(j >=0){
            a[last] = b[j];
            j--;
            last--;
        }
        return a;
        

    }
}
