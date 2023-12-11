import java.util.*;


public class Main {

    public static void main(String[] args) {
        //I introduced lambda expression to help us run test cases on leetcode questions we've done. Ndio tusidelete data we've typed kwa main method to create some space in the main method    
        IsPermutation.run();
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
public static class RemoveDuplicate1 {
    private class ListNode{

       
        private int info;
        private ListNode next;

        public ListNode(int info) {
            this.info = info;
        }

        

        @Override
        public String toString(){
            return "Node=" + info;
        }

    }
    public static String strBuild(ListNode first){
            StringBuilder sb = new StringBuilder();
            while(first.next != null){
                sb.append(first.info).append("->");
                first = first.next;
            }
            sb.append("null");

            return sb.toString();

        }

    public ListNode removeDuplicate(ListNode s){
        
        var first = s;

        if(first == null || first.next == null) return first;

        Set<Integer> set = new HashSet<>();
        
        set.add(first.info);
        
        while(first.next != null){
            if(set.contains(first.next.info)) {

                first.next = first.next.next;
                
            }else{

                set.add(first.next.info);

                first = first.next;
            }
            
        }
        return s;
    }

   
    
}

    public static class RemoveDuplicate {
    private class ListNode {
        private Integer info;


        private ListNode next;
    
        @Override
        public String toString() {
            return "Node=" + info;
        }
    }

    private static String listToString(ListNode head) {
            StringBuilder sb = new StringBuilder();
            while (head != null) {
                sb.append(head.info).append(" -> ");
                head = head.next;
            }
            sb.append("null");
            return sb.toString();
        }

    

    public ListNode removeDuplicate(ListNode s){
       var first = s;
       if(first == null || s.next == null) return first;
       
       Set<Integer> set = new HashSet<>();
       //ListNode first = s;
       set.add(first.info);
        while(first.next != null){

            if(set.contains(first.next.info)) {

                first.next = first.next.next;
                
            }else{
                set.add(first.next.info);
                first = first.next;
            }
            
            
        }
        return first;

    }
}

private static class IsPermutation {
    public boolean isPermutation(String s, String t) {
        if (s.length() != t.length()) return false;

        int[] letterCount = new int[128]; // Assuming ASCII
        for (int i = 0; i < s.length(); i++) {
            letterCount[s.charAt(i)]++;
        }

        for (int i = 0; i < t.length(); i++) {
            letterCount[t.charAt(i)]--;
            if (letterCount[t.charAt(i)] < 0) {
                return false;
            }
        }

        return true;
    }
}


    static Runnable IsUnique = () -> {
        IsUnique ans = new IsUnique();
        String s = "raydon";
        boolean answer = ans.isUnique3(s); // Use 'sol' to call the method
        System.out.println("Is the string given made up of only unique characters ? " + answer);

        };

        static Runnable twoSum = () -> {
        TwoSum sol = new TwoSum();
        int[] val = {22,0,11,9};
        int tgt = 9;
        int[] result = sol.twoSum(val, tgt);
        System.out.println(Arrays.toString(result));
        };

        static Runnable removeDuplicates = () -> {
        RemoveDuplicate1 test = new RemoveDuplicate1();

        RemoveDuplicate1.ListNode first = test.new ListNode(1);
        first.next = test.new ListNode(2);
        first.next.next = test.new ListNode(2);
        first.next.next.next = test.new ListNode(3);
        first.next.next.next.next = test.new ListNode(3);
        first.next.next.next.next.next = test.new ListNode(4);

    
        System.out.println("Original list: " + RemoveDuplicate1.strBuild(first));
        RemoveDuplicate1.ListNode result = test.removeDuplicate(first);
        System.out.println("List after removing duplicates: " + RemoveDuplicate1.strBuild(result));
        };

        static Runnable IsPermutation = () -> {
            IsPermutation test = new IsPermutation();
            String s = "raydon";
            String t = "donraye";
            var result = test.isPermutation(s, t);
            System.out.println("Are these two strings permutations of each other? " + result);
        };

        

        

}
  


