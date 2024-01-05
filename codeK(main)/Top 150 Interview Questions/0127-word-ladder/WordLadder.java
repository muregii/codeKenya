import java.util.*;

public class WordLadder {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
       
        Set<String> set = new HashSet<>(wordList);
        if(!set.contains(endWord)) return 0;

        var changes = 1;

        Set<String> visited = new HashSet<>();
        visited.add(beginWord);

        Set<String> fromTheStart = new HashSet<>();
        fromTheStart.add(beginWord);
       
        Set<String> fromTheEnd = new HashSet<>();
        fromTheEnd.add(endWord);

        while(!fromTheStart.isEmpty() && !fromTheEnd.isEmpty()){
            if(fromTheStart.size() > fromTheEnd.size()){
                Set<String> temp = fromTheStart;
                fromTheStart = fromTheEnd;
                fromTheEnd = temp;
            }

            Set<String> temp = new HashSet<>();
            for(var word : fromTheStart){
                char[] arrChars = word.toCharArray();
                for(int i = 0; i < arrChars.length; i++){
                    for(char k = 'a'; k <= 'z'; k++){
                        char tmp = arrChars[i];
                        arrChars[i] = k;

                        String target = String.valueOf(arrChars);

                        if(fromTheEnd.contains(target)){
                            return changes + 1;
                        }

                        if(!visited.contains(target) && set.contains(target)){
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
        return 0;
    }
}