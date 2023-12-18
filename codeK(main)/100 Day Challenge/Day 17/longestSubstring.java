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
        HashMap<Character, Integer> stringMap = new HashMap<>();
        //s = {a,b,c,a,b,c,b,b}
        for (int i = 0; i < s.length(); i++) {
            if (stringMap.containsKey(s.charAt(i))) {
                return maxLength = stringMap.get(s.charAt(i));
            } else {
                stringMap.put(s.charAt(i), i);
            }
        }
        return maxLength;
    }
}