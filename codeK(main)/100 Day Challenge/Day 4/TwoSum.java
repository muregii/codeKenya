import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        // numbers [] = {2, 7, 11, 15 }
        //The number we want = 9;
       Map<Integer, Integer> indexToNumber = new HashMap<>();
       //when i = 0:  9. (9 - 2 = 7); 7 is not in our map because ndio tumeanza tu, hakuna kitu kwa map bado, so use .put() to store nums[i] which is 2 as a Key in our map, and 0, the value of i = 0 as the Value  to complete the KEY, VALUE pairing for our HashMap
        //when i = 1:  9. (9 - 7 = 2) : 2 is in our indexToNumber map as a Key from the previous step, so execute the return int[] instructions under the if statement
       for(int i = 0; i < nums.length; i++){
           if(indexToNumber.containsKey(target - nums[i])) //Note that 7 was not yet in our map when i=0. We were yet to put anything in our map. So this condition was only true when i = 1;
            return new int[]{indexToNumber.get(target - nums[i]), i}; // .get() returns the value associated with the Key (target - nums[i]) = 2) from our updated map, in this case 0,
       
        indexToNumber.put(nums[i], i);     
          // (KEY) 2, (VALUE) 0  
          
           
    }
    throw new IllegalArgumentException("Error");
    }
}
    