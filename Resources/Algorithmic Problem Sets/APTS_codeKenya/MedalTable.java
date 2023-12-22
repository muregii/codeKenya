import java.util.*;

 
public class MedalTable {
 
    Map<String, int[]> MedalMap = new HashMap<>();
 
    private class Comp implements Comparator<String> {

        public int compare(String a, String b) {        
 
            for (int j = 0; j < MedalMap.get(a).length; j++) {
 
                if (MedalMap.get(a)[j] > MedalMap.get(b)[j]) {
                    return -1;
                } else if (MedalMap.get(a)[j] < MedalMap.get(b)[j]) {
                    return 1;
                }
               
            }
 
            return a.compareTo(b);
 
        }
    }
 
    public String[] generate(String[] results) {
 
        for (String result : results) {
            String[] medals = result.split(" ");
 
            for (int i = 0; i < medals.length; i++) {
                MedalMap.putIfAbsent(medals[i], new int[3]);
                MedalMap.get(medals[i])[i]++;
 
            }
        }
 
        String[] nations = new String[MedalMap.size()];
 
        int k = 0;
        for (String key : MedalMap.keySet()) {
            nations[k] = key;
            k++;
        }
 
        Arrays.sort(nations, new Comp());
 
        // Now format it
 
        for (int i = 0; i < nations.length; i++) {
            int[] medals = MedalMap.get(nations[i]);
 
            String finalString = nations[i];
            for (int count : medals) {
                finalString = String.join(" ", finalString, Integer.toString(count));
            }
 
            nations[i] = finalString;
        }
 
        return nations;
 
    }
}

/*

public static ListNode mystery (ListNode listA, ListNode listB) {
    ListNode myList = new ListNode(listA.info);
    ListNode current = myList;
    listA = listA.next;

    while(listA != null) {
        current.next = new ListNode(listA.info);
        current = current.next;
        listA = listA.next;
    }

    while(listB != null) {
        current.next = new ListNode(listB.info);
        current = current.next;
        listB = listB.next;
    }
    return myList;
} */