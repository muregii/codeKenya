import java.util.*;

/*A transformation sequence from word beginWord to word endWord using a dictionary
 called wordList is a sequence of words [beginWord] -> s1 ->s2 -> sk
 such that:
 Every adjacent pair of words differs by a single letter.
 Every si for 1 <= i <= k  is in wordList. beginWord need not be in wordList.
 sk == endWord.

 Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence
 from beginWord to endWord, or 0 if no such sequences exist.

 Test cases:
 beginWord = "hit",     endWord = "cog",    wordList = ["hot", "dot", "dog", "lot", "cog"]
 Output:    5
  
 */

 public class WordLadderProblem {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        //what are the vertices? -> they are the words. 
        Map<String, HashSet<String>> aList = makeGraph(beginWord, wordList);
        //BFS it
        Queue<String> toExplore = new LinkedList<>();
        Map<String, Integer> ladderLen = new HashMap<>();

        toExplore.add(beginWord);
        ladderLen.put(beginWord, 1);

        while(toExplore.size() > 0) {
            String current = toExplore.remove();
            for(String other : aList.get(current)) {
                if(!ladderLen.containsKey(other)) {
                    ladderLen.put(other, ladderLen.get(current) +1);
                    toExplore.add(other);
                }
            }

        }

        return ladderLen.getOrDefault(endWord, 0);//return length of the shortest ladder
        //draw an edge between two words "vertices" if they differ by one letter.
        
    }

    private Map<String, HashSet<String>> makeGraph(String beginWord, List<String> wordList) { //an adjacency list implementation
        Map<String, HashSet<String>> aList = new HashMap<>();
        for(String w: wordList) {
            aList.put(w, new HashSet<>());
            for(String other: wordList) { //building this graph is O(N^2), thus this is the major part that will slow down your code...
                if(oneOff(w, other)) {
                    aList.get(w).add(other);
                }
            }
        }



        return aList;
    }

    private boolean oneOff(String w, String other) {
        int numOff = 0;

        for(int i = 0; i < Math.min(w.length(), other.length()); i++){
            if(w.charAt(i) != other.charAt(i)) {numOff++; }
        }
        return (((numOff == 1) && (w.length() == other.length())));
    }
  }