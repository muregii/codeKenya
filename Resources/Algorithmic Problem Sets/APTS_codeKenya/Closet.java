import java.util.*;

public class Closet {
    public String anywhere(String[] list) {
        String result = helper(list, 0);
        return result;

    }

    public String helper(String[] first, int count) {
        if(first.length == 1) {
            return first[0];
        }
        String left = "";
        String right = "";

        if(first.length > 2) {
            left = helper(Arrays.copyOfRange(first, 0, first.length / 2), count+1);
            right = helper(Arrays.copyOfRange(first, first.length / 2, first.length), count+1);
        }
        else {
            left = first[0];
            right = first[1];
        }
        if(left.equals("") || right.equals("")) {
            return "";
        }
        HashSet<String> trial = new HashSet<>();

        for(String w: left.split(" ")) {
            if(!trial.contains(w)) {
                trial.add(w);
            }
        }

        for(String w: right.split(" ")) {
            if(!trial.contains(w)) {
                trial.add(w);
            }
        }

        if(trial.size()==0){
            return "";
        }

        String[] var = new String[trial.size()];
        trial.toArray(var);

        if(count==0) {
            Arrays.sort(var);
        }

        return String.join(" ", var);
    }
}