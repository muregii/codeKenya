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
class Solution {
    public boolean isAnagram(String s, String t) {
       if (s.length() != t.length()) return false; //If length of the strings not equal then definately not anagrams - base case

       int[] count_char = new int[26];//

       for (int i = 0; i < s.length(); i++){
            count_char[s.charAt(i) - 'a']++;
            count_char[t.charAt(i) - 'a']--;
       }

       for (int i : count_char){
            if (i != 0) return false;
       }
       return true;
    }
}