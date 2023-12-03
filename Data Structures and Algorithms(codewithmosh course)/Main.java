import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class Main {

    public static void main(String[] args) {
        Solution sol = new Solution();
    
        int[] val = {22, 0, 11, 9};
        int tgt = 9;
        int[] result = sol.twoSum(val, tgt); // Use 'sol' to call the method
        System.out.println(Arrays.toString(result));
    }

   public static class Solution {
   

    public static int[] twoSum(int[] nums, int target) {
       //Key | Value  nums [] = [2,7,11,15] 
        //                       0 1 2 3 
        Map<Integer, Integer> map = new HashMap<>();
        for(int i = 0; i < nums.length; i++){
            if(map.containsKey(target - nums[i])) return new int[] {map.get(target - nums[i]), i };
        map.put(nums[i], i); //(Key)2 | (Value) 0
        }
        throw new IllegalArgumentException();
    }

}
  

}
