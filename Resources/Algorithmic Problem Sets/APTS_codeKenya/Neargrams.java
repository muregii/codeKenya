import java.util.*;

public class Neargrams {
    public int numOfNeargrams(String words) {
        
        String[] wordList = words.split("\\s+");
        
        
        List<Map<Character, Integer>> freqs = new ArrayList<>();
        for (String word : wordList) {
            Map<Character, Integer> freq = new HashMap<>();
            for (char c : word.toCharArray()) {
                freq.put(c, freq.getOrDefault(c, 0) + 1);
            }
            freqs.add(freq);
        }
        
        
        int count = 0;
        Set<Integer> used = new HashSet<>();
        for (int i = 0; i < wordList.length; i++) {
            for (int j = i + 1; j < wordList.length; j++) {
                if (i != j && isNeargram(freqs.get(i), freqs.get(j))) {
                    int hash = Objects.hash(i, j); 
                    if (!used.contains(hash)) {
                        count++;
                        used.add(hash);
                    }
                }
            }
        }
        return count;
    }
    
    private boolean isNeargram(Map<Character, Integer> freq1, Map<Character, Integer> freq2) {
        if (freq1.size() != freq2.size()) {
            return false;
        }
        for (char c : freq1.keySet()) {
            int count1 = freq1.get(c);
            int count2 = freq2.getOrDefault(c, 0);
            if (Math.abs(count1 - count2) > 1) {
                return false;
            }
        }
        return true;
    }
}
