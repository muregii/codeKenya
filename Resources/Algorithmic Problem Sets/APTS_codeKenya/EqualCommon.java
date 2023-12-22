import java.util.*;
import java.util.ArrayList;

public class EqualCommon {
    public String[] matches(String[] a1, String[] a2) {
        // change this code
       Map<String, Integer> firstmap= new HashMap<>();
       Map<String, Integer> secondmap= new HashMap<>();
       ArrayList<String> matched = new ArrayList<>();
              
        for(int i=0;i<a1.length;i++){
            String currletter = a1[i];
                if(!firstmap.containsKey(currletter)) {
                    firstmap.put(currletter, 1);
                }
            secondmap.put(currletter, secondmap.get(currletter)+1);
            }
        for(String a: a1){
            if(firstmap.containsKey(a) && secondmap.containsKey(a)) {

            if(firstmap.get(a) == secondmap.get(a)){
                matched.add(a);
                }
            }
        }

    Collections.sort(matched);
     String[] ans = matched.toArray(new String[0]);
     return ans;

    }
    public static void main(String[] args) {
        EqualCommon obj = new EqualCommon();
        String[] a1 = {"Raydon", "Alex", "Michael"};
        String[] a2 = {"Angela", "Bleige", "Sydney"};
        System.out.println(Arrays.toString(obj.matches(a1, a2)));
    }
}