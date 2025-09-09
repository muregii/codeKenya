import java.util.*;


public class Unique {
    // Implement an algorithm to determine if a string has all unique characters. (What if you cannot use additional data structures)
    public boolean isUnique(String string){
        //"raydon y" --> True
        //{r a y d o n } false
        Set<Character> set = new HashSet<>();
        for(int i = 0; i < string.length(); i++){
            if(set.contains(string.charAt(i))) return false;
        set.add(string.charAt(i));
        }
        return true;
    }

    public boolean isUnique5(String string){
        //pigeon hole 
        //{ }
        if(string.length() > 26) return false;

        //ASCII calculations , Bitwise AND na Bitwise shifting
        for(int i = 0; i < string.length(); i++){
            int flag = 0;
            // 00 |00
            // abc
            int val = string.charAt(i) - 'a'; // b --> 99 - 97 = 2

            if((flag & (1 << val))  > 0  )  return false; //1  // 100 = 4 | 000 -- >   0 & 1  = 0 

            flag |= (1<<val);
        }
        return true;
    }
}
