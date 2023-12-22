import java.util.*;

public class TxMsg {
    public String getMessage(String original) {
      // code here
      Set<String> vowels = new HashSet<>(Arrays.asList(new String[] {"a", "e","i","o","u"}));
      //--> "text message" --> "text" "message" tx msg
      String[] words = original.split(" ");
      String word = "";

      for(int i=0; i< words.length; ++i) {
        for(int j = 0; j < words[i].length(); j++) {
            if(!vowels.contains(words[i].substring(j, j+1))) {
                if(j==0) {
                    word += words[i].substring(j, j+1);
                    continue;
                }
                else if(vowels.contains(words[i].substring(j-1,j))) {
                    word += words[i].substring(j, j+1);
                }
            }
        }
        if(word.length() != 0) {
            words[i] = word;
        }
        word ="";
      }
      return String.join(" ", words);
    }
    public static void main(String[] args) {
        TxMsg obj = new TxMsg();

        String message = "text message";
        String message1 = "ps i love u";

        System.out.println(obj.getMessage(message));
        System.out.println(obj.getMessage(message1));

    }
 }