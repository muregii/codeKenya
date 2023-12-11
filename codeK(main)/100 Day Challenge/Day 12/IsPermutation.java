//This question is from Arrays in cracking the coding interview.

//Given two strings, write a method to determine if one is a permutation of the other

public class IsPermutation {
    public boolean isPermutation (String s, String t){
        
        for(var ch : s){
            char str = t.charAt(0);
            if(ch == str){
                t.remove(0);
            }
            if(t.length() == 0) return true;

            return false;
        }
        
    }
}
