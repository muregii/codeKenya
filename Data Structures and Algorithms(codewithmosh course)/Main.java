import java.util.*;

public class Main {

    public static void main(String[] args) {
        //I introduced lambda expression to help us run test cases on leetcode questions we've done. Ndio tusidelete data we've typed kwa main method to create some space in the main method    
        IsUnique.run();
    }

    public static class Unique {
        // Implement an algorithm to determine if a string has all unique characters. (What if you cannot use additional data structures)
        //"raydon" -> true 
        public boolean isUnique(String string){
            //{ r, a, y, d , o, n, n}
            Set<Character> set = new HashSet<>();
    
            for(int i = 0; i < string.length(); i++){
                if(set.contains(string.charAt(i))) return false;
                set.add(string.charAt(i));
            }
            //{ r, a, y, d, o, n, }
            return true;
            
        }
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
        // r , a, y, d, o, n, o
        for(var ch : str){
            if(map.contains(ch))  return false; 
        map.add(ch); 
        }
        
        return true;
        }

        public boolean isUnique4(String string){
            //"raydon y" --> True
            //{r a y d o n } false
            Set<Character> set = new HashSet<>();
            for(int i = 0; i < string.length(); i++){
                if(set.contains(string.charAt(i))) return false;
            set.add(string.charAt(i));
            }
            return true;
        }
    

    public  boolean isUnique1(String string){
       // raydon
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

    public boolean isUnique5(String string){
        //pigeon hole 
        //{ }
        if(string.length() > 26) return false;
        int flag = 0; 
        //ASCII calculations , Bitwise AND na Bitwise shifting
        for(int i = 0; i < string.length(); i++){ 
            
            // 00 |00
            // abc
            int val = string.charAt(i) - 'a'; // b --> 99 - 97 = 2
            
            if((flag & (1 << val))  > 0  ) {
                 return false;
            } //1  // 100 = 4 | 000 -- >   0 & 1  = 0 
               
            flag |= (1<<val);
        }
        return true;
    }

    public boolean isUnique3(String string){
        //pigeon hole principle
        if(string.length() > 26) return false;
        // abc
        int flag = 0;
        for(int i = 0; i < string.length(); i++){
            // ASCII a -> 97 - 97 = 0 b -> 98 -97 = 1 c = 2
            int val = string.charAt(i) - 'a';
            // 1 & 1 = 1
            // 1 & 0 = 0
            // a & b = 0
            //|b    99-97 = 10-->  | 0
            if((flag & (1<< val)) > 0 ){
                return false;
            }  
            flag |= (1<<val); // 0 | 100 = 1
        }
        return true;

    }
}

        static Runnable IsUnique = () -> {
        IsUnique ans = new IsUnique();
        String s = "raydon";
        boolean answer = ans.isUnique5(s); // Use 'sol' to call the method
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
  


