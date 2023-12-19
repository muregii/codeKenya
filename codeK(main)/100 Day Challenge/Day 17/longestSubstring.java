//Longest substring without repeating characters - Leetcode question
import java.util.HashMap;

class LongestSubstring {
    public static void main(String[] args) {
        String s = "abcabcbb";
        int result = lengthOfLongestSubstring(s);
        System.out.println(result);
    }
    public static int lengthOfLongestSubstring(String s) {
        int maxLength = 0;
        HashMap<Character, Integer> stringMap = new HashMap<>();//new HashMap
        //s = {a,b,c,a,b,c,b,b}
        for (int i = 0; i < s.length(); i++) { //loops through the string
            if (stringMap.containsKey(s.charAt(i))) { //Checks if the char is already in the HashMap
                return maxLength = i - stringMap.get(s.charAt(i)); //returns current value of i - (index of the already initial char)
            } else {
                stringMap.put(s.charAt(i), i);//if not repeated, adds the char to the map
            }
        }
        return maxLength; // Returns the max length of the substring
    }
}