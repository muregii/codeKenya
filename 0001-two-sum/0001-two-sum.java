//Video explanation: https://youtu.be/4UFzvlOq8F8?si=msCPNu9SZs96M64R
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        
        for(int i = 0; i < nums.length; ++i) {
            int complement = target - nums[i];
            if(map.containsKey(complement)) return new int[]{ map.get(complement), i};
            map.put(nums[i], i);
                
        }
        throw new IllegalArgumentException("Try a different number");
        
}
}
