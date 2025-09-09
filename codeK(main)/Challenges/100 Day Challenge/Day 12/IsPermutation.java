//This question is from Arrays in cracking the coding interview.

//Given two strings, write a method to determine if one is a permutation of the other


public class IsPermutation {
       public static void main(String[] args) {
    //I introduced lambda expression to help us run test cases on leetcode questions we've done. Ndio tusidelete data we've typed kwa main method to create some space in the main method    
        IsPermutation.run();
}
    public boolean isPermutation (String s, String t){
        
       if(s.length() != t.length()) return false;
       int[] letterCount = new int[128];

       for(int i = 0; i < s.length(); ++i){
        letterCount[s.charAt(i)]++;
        
        System.out.println(letterCount[s.charAt(i)]);
       }

       for(int i = 0; i < s.length(); ++i){
        letterCount[t.charAt(i)]--;
        System.out.println(letterCount[t.charAt(i)]);
        if(letterCount[t.charAt(i)] < 0) return false;
        
       }
       return true; 
        
    }

 

static Runnable IsPermutation = () -> {
    IsPermutation test = new IsPermutation();
    String s = "rayo";
    String t = "rayd";
    var result = test.isPermutation(s, t);
    System.out.println("Are these two strings permutations of each other? " + result);
};
}
