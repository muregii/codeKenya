//import java.util.*;

class Solution {
    public int strStr(String haystack, String needle) {
        int firstNeedleIndex = 0;
        int[] count_char = new int[26];

        //Map<Character, Integer> haystackMap = new HashMap<>();


        for (int i = 0; i < haystack.length()-1; i++) {
            if (haystack.charAt(i) == needle.charAt(0)) {
                firstNeedleIndex = i;
            }
        
        }
        for (int i = firstNeedleIndex; i < needle.length(); i++) {
            count_char[haystack.charAt(i) - 'a']++;
            count_char[needle.charAt(i) - 'a']--;
        }

        for (int i : count_char) {
            if (i == 0) {
                return firstNeedleIndex;
            } else {
                return -1;
            }
        }
        
        return firstNeedleIndex;
    }
}