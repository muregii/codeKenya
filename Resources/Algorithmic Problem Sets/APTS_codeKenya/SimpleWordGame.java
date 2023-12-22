import java.util.*;

public class SimpleWordGame {
    public int points(String[] player, 
                      String[] dictionary) {
        // you write code here
        HashSet<String> result = new HashSet<>(Arrays.asList(dictionary));
        int val = 0;

        for(String word: player) {
            if(result.contains(word)) {
                val+= Math.pow(word.length(), 2);
                result.remove(word);
            }
        }
        return val;
    }

    //pvsm
    public static void main(String[] args) {
        SimpleWordGame obj = new SimpleWordGame();
        String[] player = {"cat", "dog", "hesed"};
        String[] dictionary = {"cat", "dog"};
        int points = obj.points(player, dictionary);
        System.out.println("Your score is: " + points);
;
    }
}