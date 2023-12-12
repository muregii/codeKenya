//This question is from Arrays in cracking the coding interview.

//Given two strings, write a method to determine if one is a permutation of the other

public class IsPermutation {
    public boolean isPermutation (String s, String t){
        
       if(s.length() != t.length()) return false;
       int[] letterCount = new int[128];

       for(int i = 0; i < s.length(); ++i){
        letterCount[s.charAt(i)]++;
       }

       for(int i = 0; i < s.length(); ++i){
        letterCount[t.charAt(i)]--;
        if(letterCount[t.charAt(i)] > 0) return false;
       }
       return true;

       

       
        
    }
}
