import java.util.*;

public class Main {

    public static void main(String[] args) {
        //I introduced lambda expression to help us run test cases on leetcode questions we've done. Ndio tusidelete data we've typed kwa main method to create some space in the main method
        isUnique.run();
        twoSum.run();
    }

    public static class TwoSum{

        public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> complements = new HashMap<>();
        for (int i = 0; i < nums.length; i++){
            Integer complementIndex = complements.get(nums[i]);
            if (complementIndex != null){
                return new int[]{complementIndex, i};
            }
            complements.put(target - nums[i], i);
        }
        return nums;
    
    }

    public int[] twoSum1(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        
        for(int i = 0; i < nums.length; ++i) {
            int complement = target - nums[i];
            if(map.containsKey(complement)) return new int[]{ map.get(complement), i};
            map.put(nums[i], i);
                
        }
        throw new IllegalArgumentException("Try a different number");
        
        }

    }
    

   public static class IsUnique{
    public boolean isUnique(String string){
       
        Set<Character> map = new HashSet<>();
        var str = string.toCharArray();
        for(var ch : str){
            if(map.contains(ch))  return false; 
        map.add(ch); 
        }
        
        return true;
        }
    

    public  boolean isUnique1(String string){
       
        var left = 0;
        var right = string.length()-1;

            while(left < right){
                var l = string.charAt(left);
                var r = string.charAt(right);

                if(l == r) return false;

                left++;
                right--;
            }
            return true;
         
    }

    public boolean isUnique2(String string) {

        if (string.length() > 26) { 
            return false;
        }
    
        int checker = 0;
        for (int i = 0; i < string.length(); i++) {
            int val = string.charAt(i) - 'a'; 
            if ((checker & (1 << val)) > 0) { 
                return false; 
            }
            checker |= (1 << val); 
        }
    
        return true;
    }
}

        static Runnable isUnique = () -> {
        IsUnique ans = new IsUnique();
        String s = "raydon";
        boolean answer = ans.isUnique1(s); // Use 'sol' to call the method
        System.out.println("Is the string given made up of only unique characters ? " + answer);

        };

        static Runnable twoSum = () -> {
        TwoSum sol = new TwoSum();
        int[] val = {22,0,11,9};
        int tgt = 9;
        int[] result = sol.twoSum(val, tgt);
        System.out.println(Arrays.toString(result));
        };

}
  


