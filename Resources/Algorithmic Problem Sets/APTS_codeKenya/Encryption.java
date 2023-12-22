import java.util.HashMap;

public class Encryption {
    public String encrypt (String message) {
        HashMap<String, String> encrypted = new HashMap<>();
        int start = 97;//Where did this magic number come from?
        String indexing = "";//?
        String val = "";//?

        for(int i=0;i<message.length();i++){//looping through the message.
            indexing = message.substring(i, i+1);// create substrings
            if(encrypted.containsKey(indexing)) {// check if encrypted key has been mapped into the indexing var.
                val += encrypted.get(indexing);//map the indexed key to the value variable
            }
            else{
                encrypted.put(indexing, String.valueOf((char) start));//?
                start +=1;//?
                val += encrypted.get(indexing);
            }
        }
     return val;    
    }

    
}