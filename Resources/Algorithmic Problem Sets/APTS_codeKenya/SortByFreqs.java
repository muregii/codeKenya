import java.util.*;

public class SortByFreqs {
    public String[] sort(String[] data) {
        // fill in code here
        TreeMap<String, Integer> sortTree = new TreeMap<>();
        for(String w: data){
            sortTree.putIfAbsent(w, 0);
            sortTree.put(w, sortTree.get(w)+1);
            
        }
        ArrayList<Map.Entry<String, Integer>> list1 = new ArrayList<>(sortTree.entrySet());
        Collections.sort(list1, Collections.reverseOrder(Comparator.comparing(Map.Entry::getValue)));

        String[] data1 = new String[list1.size()];
        for(int k = 0; k < list1.size(); k++){
            data1[k] = list1.get(k).getKey();
        }
        return data1;
    }

    
 }