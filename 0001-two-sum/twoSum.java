import java.util.HashMap;
import java.util.Map;
import java.util.Arrays;

class Solution {
    public static void main (String[] args) {
        int[] val = {22,0,11,9};
        int tgt = 9;
        int[] result = twoSum(val, tgt);
        System.out.println(Arrays.toString(result));
    } 

    public static int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> complements = new HashMap<>();
        for (int i = 0; i < nums.length; i++){
            Integer complementIndex = complements.get(nums[i]);
            if (complementIndex != null){
                return new int[]{i, complementIndex};
            }
            complements.put(target - nums[i], i);
        }
    return nums;
    }

}