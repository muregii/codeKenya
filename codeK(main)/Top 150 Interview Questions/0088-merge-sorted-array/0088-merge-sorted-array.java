class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        var i = m-1;
        var j = n-1;
        var last = m+n-1;
//      nums1 = [1,2,2,3,5,6], m = 3, nums2 = [2,5,6], n = 3
//      [1,2,2,3,5,6]

        //i = 0 j = 0. last = 0
        while(i >= 0 && j >= 0){
            if(nums1[i] > nums2[j]){
                nums1[last] = nums1[i];
                i--;
            }else{
                nums1[last] = nums2[j]; 
                j--; 
            }
            last--;
        }

        
        while(j >= 0){
            nums1[last] =  nums2[j];
            j--;
            last--;
        }
    }
}