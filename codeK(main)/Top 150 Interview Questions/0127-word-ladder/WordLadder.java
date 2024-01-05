import java.util.*;

public class WordLadder {
    public String ladderExists(String[] words, String from, String to) {
        List<String> wordList = Arrays.asList(words);
        Set<String> set = new HashSet<>(wordList);
        if (!set.contains(to)) return "no";

        int changes = 1;
        Set<String> visited = new HashSet<>();
        visited.add(from);

        Set<String> fromTheStart = new HashSet<>();
        fromTheStart.add(from);

        Set<String> fromTheEnd = new HashSet<>();
        fromTheEnd.add(to);

        while (!fromTheStart.isEmpty() && !fromTheEnd.isEmpty()) {
            if (fromTheStart.size() > fromTheEnd.size()) {
                Set<String> temp = fromTheStart;
                fromTheStart = fromTheEnd;
                fromTheEnd = temp;
            }

            Set<String> temp = new HashSet<>();
            for (String word : fromTheStart) {
                char[] arrChars = word.toCharArray();
                for (int i = 0; i < arrChars.length; i++) {
                    for (char k = 'a'; k <= 'z'; k++) {
                        char tmp = arrChars[i];
                        arrChars[i] = k;

                        String target = String.valueOf(arrChars);

                        if (fromTheEnd.contains(target)) {
                            return "yes";
                        }

                        if (!visited.contains(target) && set.contains(target)) {
                            temp.add(target);
                            visited.add(target);
                        }
                        arrChars[i] = tmp;
                    }
                }
            }
            fromTheStart = temp;
            changes++;
        }
        return "no";
    }
}
