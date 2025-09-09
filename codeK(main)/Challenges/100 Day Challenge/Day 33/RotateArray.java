

public class RotateArray {
    
        public void rotate(int[] nums, int k) {
        /* REVERSE METHOD
            4. Handle case where k > array length
            1.Reverse the whole array
            2.Reverse the first k elements
            3.Reverse the remaining n-k elements, where n is the length of the array.
          
            */
            k = k % nums.length;
            reverse(nums, 0, nums.length-1);
            reverse(nums, 0, k-1);
            reverse(nums, k, nums.length -1);
        }
    
        private void reverse(int[] nums, int beginning, int end){
            while(beginning < end){
                int tempHold = nums[beginning];
                nums[beginning] = nums[end];
                nums[end] = tempHold;
    
                beginning++;
                end--;
            }
        
    
    
    }
}
