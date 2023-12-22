import java.util.*;

public class IsomorphicWords {
    public static void main (int[] args){
        IsomorphicWords obj = new IsomorphicWords();
        String[] words = {"Raydon", "Angela"};
            //String[] words = {"Raydon", "Angela"};
        System.out.println((obj.countPairs(words)));
        }
    public int countPairs(String[] words) {
        String [] letters = {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"};
        //code here
        int result = 0;
        HashMap <String, String> myHashset = new HashMap<>();
        HashMap<String, Integer> mySet = new HashMap<>();
        
        String str = "";
        int count = 0;
        for(String w: words) {
        str = "";
        count = 0;
        myHashset = new HashMap<>();
        for(int i=0;i<w.length();i++) {   
            if(!myHashset.containsKey(w.substring(i, i+1))) {
                myHashset.put(w.substring(i, i+1), letters[count++]);
            }
            str += myHashset.get(w.substring(i, i+1));
        }
        if(mySet.containsKey(str)) {
            mySet.replace(str, mySet.get(str)+1);

        }
        else {
            mySet.put(str, 1);
        }
    }

        for(String key: mySet.keySet()) {
            if(mySet.get(key) != 1) {
                count = 1;
                for(int i=mySet.get(key)-1; i<= mySet.get(key); i++){
                    count *= i;
                }
                result += count / 2;
            }
        }
        return result;
    }
    public static void main(String[] args) {
        IsomorphicWords obj = new IsomorphicWords();
        String[] words = {"foo", "bar", "baz", "boo", "foobar", "foobaz", "abcde"};
        int count = obj.countPairs(words);
        System.out.println("Number of pairs: " + count);
    }
    
     
}

