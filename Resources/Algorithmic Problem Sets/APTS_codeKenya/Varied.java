import java.util.*;

public class Varied {
    public String[] variedStrings(String[] words) {
      // TO DO: fill in code here  
      List<String> result = new ArrayList<>();
        for (String word : words) {
            Map<Character, Integer> charCount = new HashMap<>();
            boolean isUnique = true;
            for (char c : word.toCharArray()) {
                if (charCount.containsKey(c)) {
                    charCount.put(c, charCount.get(c) + 1);
                } else {
                    charCount.put(c, 1);
                }
            }
            for (int count : charCount.values()) {
                if (count > 1) {
                    isUnique = false;
                    break;
                }
            }
            if (isUnique) {
                result.add(word);
            }
        }
        return result.toArray(new String[0]);
    }
  }


