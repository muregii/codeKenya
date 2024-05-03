 /*
        Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
        */
        
        //attempting the use of a bidirectional  BFS to cut down complexity to O(M^2 * N(1/2))
         //Ok now improve the code with bidirectional BFS

import java.util.*;

class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
       
        Set<String> set = new HashSet<>(wordList);
        if(!set.contains(endWord)) return 0;

        var changes = 1;

        Set<String> visited = new HashSet<>();
        //visited.add(beginWord);

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

        /*Set<String> visited = new HashSet<>();
        visited.add(beginWord);

        Queue<String> queue = new LinkedList<>();
        queue.add(beginWord); 
       
        while(!queue.isEmpty()){
            int lengthOfQueue = queue.size();
            for(int i = 0; i < lengthOfQueue; i++){
                String firstWordInTheQueue = queue.poll();
                if(firstWordInTheQueue.equals(endWord)) return changes;

                for(int j = 0; j < firstWordInTheQueue.length(); j++){
                    for(char k = 'a'; k <= 'z'; k++){
                        char[] array = firstWordInTheQueue.toCharArray(); // {'m', 'e'}
                        array[j] = k; //up to ze then upto mz, just checking

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
        return 0;*/

    }
   
}
