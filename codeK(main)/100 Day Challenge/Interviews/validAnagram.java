/*Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
*/

//using the frequency array method

import java.util.HashMap;

//using HashMap
class Answer{
     public boolean isAnagram(String s, String t) {
          if (s.length() != t.length()) return false;

          HashMap<Character, Integer> map1 = new HashMap<>();

          for (int i = 0; i < s.length(); i++) {
               if (map1.containsKey(s.charAt(i))) {
                    map1.put(s.charAt(i), map1.get(s.charAt(i)) + 1);
               } else {
                    map1.put(s.charAt(i), 1);
               }
          }
          for (int i = 0; i < t.length(); i++) {
               if (map1.containsKey(t.charAt(i))) {
                    map1.put(t.charAt(i), map1.get(t.charAt(i)) - 1);
               } else {
                    return false;
               }
          }
          for (Character key : map1.keySet()) {
               if (map1.get(key) != 0) return false;
          }
          return true;
     }

static Runnable AnagramUsingFreqCounter = () -> {
class Solution {
    public boolean isAnagram(String s, String t) {
       if (s.length() != t.length()) return false; //If length of the strings not equal then definately not anagrams - base case

       int[] count_char = new int[26];//

       for (int i = 0; i < s.length(); i++) {
            count_char[s.charAt(i) - 'a']++;
            count_char[t.charAt(i) - 'a']--;
       }

       for (int i : count_char) {
            if (i != 0) return false;
       }
       return true;
          }
     }
};
}