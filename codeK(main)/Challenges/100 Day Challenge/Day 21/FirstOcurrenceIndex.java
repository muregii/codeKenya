/*

  * Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
  * or -1 if needle is not part of haystack.

  * Example 1:

  * Input: haystack = "sadbutsad", needle = "sad"
  * Output: 0
  * Explanation: "sad" occurs at index 0 and 6.
  * The first occurrence is at index 0, so we return 0.
  * 
  * Example 2:

  * Input: haystack = "leetcode", needle = "leeto"
  * Output: -1
  * Explanation: "leeto" did not occur in "leetcode", so we return -1.
  * 
*/

//import java.util.*;

class FirstOccurrenceIndex {
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

//Using indexOf

class Solution {
    public int strStr(String haystack, String needle) {
        if (needle.length() > haystack.length()) return -1;
        for (int i = 0; i <= haystack.length() - needle.length(); i++) {
            if (haystack.substring(i, i + needle.length()).equals(needle)) {
                return i;
            }
        }

        return -1;
    }
}