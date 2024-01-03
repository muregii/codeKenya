import java.util.*;
/* So, doubling down on my area assigned to specialize. Graphs💀💀💀

Time spent today just kuelewa swali na kuthink about this question: 4 hrs

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
        //Using Bidirectional BFS O(M^2 * N(1/2))
        public int ladderLength(String beginWord, String endWord, List<String> wordList) {
            Set<String> set = new HashSet<>(wordList);
            if(!set.contains(endWord)) return 0;
            var changes = 1;

            Set<String> fromTheStart = new HashSet<>();
            Set<String> fromTheEnd = new HashSet<>();
            Set<String> visited = new HashSet<>();

            fromTheStart.add(beginWord);
            fromTheEnd.add(endWord);

            //swap
          
            while(!fromTheEnd.isEmpty() && !fromTheStart.isEmpty()){
                if(fromTheStart.size() > fromTheEnd.size()){
                Set<String> temp = fromTheStart;
                fromTheStart = fromTheEnd;
                fromTheEnd = temp;
            }
            //find the word
            Set<String> temp = new HashSet<>();

            for(var word : fromTheStart){
                char[] arrChars = word.toCharArray();

                for(int i = 0; i < arrChars.length; i++){
                     for(char k = 'a'; k <= 'z'; k++){
                        var tmp = arrChars[i];
                        arrChars[i] = k;

                        String target = String.valueOf(arrChars);

                        if(fromTheEnd.contains(target)) {
                            return changes + 1;
                        }

                        if(!visited.contains(target) && set.contains(target)) {
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
