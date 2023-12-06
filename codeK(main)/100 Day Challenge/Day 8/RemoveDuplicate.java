
import java.util.*;

public class RemoveDuplicate {
    private class ListNode {
        private Integer info;

        private ListNode next;
    
        @Override
        public String toString() {
            return "Node=" + info;
        }
    }
    

    public ListNode removeDuplicate(ListNode s){
       // var first = s;
       if(s == null || s.next == null) return s;
       
       Set<Integer> set = new HashSet<>();
       ListNode first = s;
       set.add(first.info);
        while(first.next != null){

            if(set.contains(first.next.info)) {

                first.next = first.next.next;
            }else{
                set.add(first.next.info);
                first = first.next;
            }
            
            
        }
        return s;

    }
}
