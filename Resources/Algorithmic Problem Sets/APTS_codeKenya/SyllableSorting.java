import java.util.*;

public class SyllableSorting {
    public String[] sortWords(String[] words) {
       // you write code here ...
      
       ArrayList<String> sortedSyllableList = new ArrayList<>();
    for(int i = 0; i< words.length; ++i){
       String[] syllables = decompose(words[i]);
       Arrays.sort(syllables);
       sortedSyllableList.addAll(Arrays.asList(syllables));

    }
    
    words = sortedSyllableList.toArray(new String[sortedSyllableList.size()]);
    return words; 

    }
    private String[] decompose (String word) {
        ArrayList<String> syllables = new ArrayList<>();
        StringBuilder syllable = new StringBuilder();
        boolean prevVowel = false;

        for(int i = 0; i<word.length(); ++i){
            char c  = word.charAt(i);
            boolean currVowel  = isVowel(c);

            if(syllable.length() == 0 || (prevVowel && !currVowel)){
                syllables.add(syllable.toString());
                syllable.setLength(0);
            }
        
            syllable.append(c);
            prevVowel = currVowel;

        }

        return  syllables.toArray(new String[0]);
    }

    private boolean isVowel (char c){
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' ;
    }
 }
