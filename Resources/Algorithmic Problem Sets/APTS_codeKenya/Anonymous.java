
import java.util.*;
//Dijkstra algorithm.
public class Anonymous {
    public int howMany(String[] headlines, String[] messages){
        Map<String, Integer> words = new HashMap<>();
        Map<String, Integer> indexing = new HashMap<>();
        String value = "";
        int total = 0;

        for(String w: headlines){
            for(int i=0;i<w.length();i++){
                value = w.substring(i, i+1).toLowerCase();
                if(value == " "){
                    continue;
                }
                if(words.containsKey(value)){
                   words.replace(value, words.get(value) +1);

                }
                else{
                    words.put(value, 1);
                }
            }
        }

        for(String w: messages){
            indexing.putAll(words);
            for(int i=0;i<w.length();i++){
                value = w.substring(i,i+1).toLowerCase();
                if(value.equals(" ")){
                continue;
                }
                if(indexing.containsKey(value) && indexing.get(value) > 0) {
                    indexing.replace(value, indexing.get(value) - 1);
                }
                else{
                    total-=1;
                    break;
                }
            }
            total +=1;
            indexing = new HashMap<>();
        }


        return total >= 0 ? total: 0;
    }
}