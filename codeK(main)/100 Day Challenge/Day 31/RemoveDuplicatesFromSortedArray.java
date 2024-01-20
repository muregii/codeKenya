//             Input: nums = [1,1,1,2,2,3]
//             Output: 5, nums = [1,1,2,2,3,_]

public class RemoveDuplicatesFromSortedArray {
    public int removeElements(int[] nums, int val){
        if(nums.length <= 2) return nums.length;
        int j = 2;
        for(int i = 0; i < nums.length; i++){
            if(nums[i] != nums[j - 2]){
                nums[j] = nums[i];
                j++;
            }

        }
        return j;
    }
}
