
import java.util.*;

public class Solution {


    public int lengthOfLongestSubstring(String s){
        int left = 0;
        int maxLength = 0;
        
        //The hashmap stores the last index of each character encountered.
        Map<Character, Integer> charIdxMap = new HashMap<>();
        
        for(int right = 0; right < s.length(); right++){
            char currentChar = s.charAt(right);
            //if the current char has been seen before is when we update the left pointer
            if(charIdxMap.containsKey(currentChar)){
                left = Math.max(charIdxMap.get(currentChar) + 1, left);
            }
            //if it hasn't been seen before, we update our hashmap to the most current index of the character.
            charIdxMap.put(currentChar, right);
            maxLength = Math.max(maxLength, right - left + 1);
                
        }
        return maxLength;
    }

}
