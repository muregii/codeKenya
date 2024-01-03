import java.util.*;
/* So, doubling down on my area assigned to specialize. Graphs💀💀💀

Time spent today just kuelewa swali na kuthink about this question: 1 hr

 Difficulty: Hard

 * Concepts: 
 * 1. HashTable
 * 2. String
 * 3. BFS - Breadth First Search.
 * 4. Bidirectional BFS
 * 
 * This thing is like 50 lines of code bruh
 */
public class WordLadder {
    public class Solution {
        //Using Bidirectional BFS
        public int ladderLength(String beginWord, String endWord, List<String> wordList) {
            Set<
           
        }
    }
}





//Solution 1: O(M^2* N)
/*
 * class Solution {
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
 */
