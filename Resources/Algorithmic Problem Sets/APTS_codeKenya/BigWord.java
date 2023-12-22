import java.util.HashMap;
import java.util.Map;

/*In days of yore, aka BG (Before Google), 
search engines ranked webpages in part by
the number of occurrences of a word on the page.
You should write method most to determine and return
the word that occurs most often in an array of sentences.
This most frequently occurring word will be unique ---
that is you don't need to worry about two words both occuring more often than any other word.
The word returned should be all lower-case regardless of the case of letters in sentences.
Each string in sentences represents several words, each word is delimited by spaces from other words. 
Words should be considered the same without respect to case, so BIG is the same word as big, for example.
 */

 
public class BigWord {
    public String most(String[] sentences) {
        Map<String, Integer> finalword = new HashMap<>();// To avoid duplicates I presume.
        int max = 0;//?
        String mostRecurringWord = " ";//?
        String indexing;//?
        for(String s: sentences){
            for(String space: s.split(" ")){//to divide up the words in the sentence at the spacebar
                indexing = space.toLowerCase();
                if(finalword.containsKey(indexing)){// So I'm stuck here!
                    finalword.replace(indexing, finalword.get(indexing) + 1);//?
                    if(max < finalword.get(indexing)){//?
                        mostRecurringWord = indexing;
                        max = finalword.get(indexing);
                    }
                }
                else{
                    finalword.put(indexing, 1);
                }

            }
        }


        
        return mostRecurringWord; //returns the word that appeared most.
    }
    
}