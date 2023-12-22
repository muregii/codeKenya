//import java.util.*;

class Solution {
    public int strStr(String haystack, String needle) {
        int firstNeedleIndex = 0;//we'll store the index of first char of needle at haystack
        int[] count_char = new int[26]; //frequency array we'll use to compare the two strings

        //Map<Character, Integer> haystackMap = new HashMap<>();


        for (int i = 0; i < haystack.length(); i++) {
            if (haystack.charAt(i) == needle.charAt(0)) {
                firstNeedleIndex = i;
                break;
            }
        
        }
        for (int i = firstNeedleIndex; i < needle.length(); i++) {
            count_char[haystack.charAt(i) - 'a']++;
            count_char[needle.charAt(i) - 'a']--;
        }

        for (int i : count_char) {
            if (i != 0) {
                return -1;
            }
        }
        
        return firstNeedleIndex;
    }
}