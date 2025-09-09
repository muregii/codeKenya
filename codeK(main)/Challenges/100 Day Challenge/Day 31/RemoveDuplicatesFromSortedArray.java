//             Input: nums = [1,1,1,2,2,3]
//             Output: 5, nums = [1,1,2,2,3,_]
public class RemoveDuplicatesFromSortedArray {
    public int removeElements(int[] nums, int val){
        if(nums.length <= 2) return nums.length;

        int j = 2;
        for(int i = 2; i < nums.length; i++){
            if(nums[i] != nums[j - 2]){
                nums[j] = nums[i];
                j++;
            }

        }
        return j;
    }
}

/*Hints
 * Trick ni kustart from index 2 for both i and j
 * kama nums[i] ni different na j two steps back, start of the array, tunacopy sasa nums[j] into nums[i]. Then of course the increments zinawork on the data, (i++ na j++)
 * j  ndio length tutareturn pia
 */