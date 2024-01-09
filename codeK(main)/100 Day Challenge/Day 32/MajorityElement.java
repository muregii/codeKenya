//Swali interesting hapa, also found in the Top 150 interview questions
/*
 * Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
Concepts:
1. Arrays
2. HashTable
3. Divide and Conquer
4.  

*/


public class MajorityElement {
    public int majorityElement(int[] nums) {
        var size = nums.length;
        var count = 0;
        Map<Integer, Integer> map = new HashMap<>();
        for(int i = 0; i < nums.length; i++){
            if(map.containsKey(nums[i])){
                map.put(nums[i], count++);
                
            }
            map.put(nums[i], count);
            
        }

        for(var i : nums){
            if(map.get(nums[i]) > size){
                return nums[i];
            }
        }
        
        return 0;
    }
}
