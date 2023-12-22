import java.util.*;

public class StringCuts {
    public String[] filter(String[] list, int minLength) {
        // replace this with your code
        List<String> array = new ArrayList<>();

        for(int i = 0; i < list.length; ++i) {
            if(list[i].length() >= minLength) {
                if(!array.contains(list[i])){
                    array.add(list[i]);
                }
            }
        }

        String[] obj = new String[array.size()];

        for(int i = 0; i < obj.length; i++) {
            obj[i] = array.get(i);
        }

        return obj;
    }

    //psvm
    public static void main(String[] args) {
    StringCuts obj = new StringCuts();
    String[] list = {"cat", "boisterous", "enormous","enormous"};
    int minLength = 4;
    String[] results = obj.filter(list, minLength);

    for(String w: results) {
        System.out.println(w);
    }
    }
    
}
