import java.util.*;

public class WordLadder {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
    var changes = 1;
    Set<String> set = new HashSet<>(wordList);
     
    Queue<String> queue = new LinkedList<>();
      queue.add(beginWord);

    Set<String> visited = new HashSet<>();
        queue.add(beginWord);
    
    while(!queue.isEmpty()){ 
        var lengthOfQueue = queue.size();
        for(int i = 0; i < lengthOfQueue; ++i){
            var word = queue.poll();
            if(word.equals(endWord)) return changes;

            for(int j = 0; j < word.length(); ++j){
                for(int k = 'a'; k <= 'z'; ++k){
                    char array[] = word.toCharArray();
                    array[j] = (char) k;

                    String string = new String(array);
                    if(set.contains(string) && !visited.contains(string)){
                        queue.add(string);
                        visited.add(string);
                    }
                 }
            }
        }
        ++changes;
    }
    return 0;

    }
}