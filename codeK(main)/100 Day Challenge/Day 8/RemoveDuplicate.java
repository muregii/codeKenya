//Question: From LinkedLists in Cracking the coding interview: Write code to remove duplicates from an unsorted Linked List. (What is a temporary buffer is not allowed? )

import java.util.*;

public class RemoveDuplicate {
    private class ListNode {
        private Integer info;

        private ListNode next;
    
        public static String listToString(RemoveDuplicate.ListNode head){
            StringBuilder sb = new StringBuilder();
            while(head.next != null){
                sb.append(head.info).append("->");
                head = head.next;
            }
            sb.append("null");
            return sb.toString();
        }

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
