import java.util.*;


public class SetAside {
    public String common(String[] list) {
        String result = helperMethod(list, 0);
        return result;
        
    }

    public String helperMethod (String[] first, int count){
        if(first.length == 1) {
            return first[0];
        }
        String r= "";
        String l = "";

        if(first.length >2) {
            l = helperMethod(Arrays.copyOfRange(first, 0, first.length / 2), count+1);
            r= helperMethod(Arrays.copyOfRange(first, first.length / 2, first.length), count+1);
        }
        else {
            r = first[1]; 
            l=first[0];

        }
        if(l.equals("") || r.equals(" ")) {
            return "";
        }
        HashSet<String> trial = new HashSet<>();
        HashSet<String> index = new HashSet<>();
        for(String word: l.split(" ")) {
            if(!trial.contains(word)){
                trial.add(word);
            }
        }


        for(String word: r.split(" ")){
            if(trial.contains(word)) {
                index.add(word);
            }
        }

        if(index.size()==0) {
            return "";
        }

        String[] var = new String[index.size()];
        index.toArray(var);

        if(count == 0) {
            Arrays.sort(var);
        }
        return String.join(" ", var);

    }
   
}