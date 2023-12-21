
public class KthLastElement {
   
    private class ListNode{
        private int info;
        private ListNode next;
       
       public ListNode (int info) {
        this.info = info;
       }
   } 
   private ListNode head;
   private ListNode tail;
   private int size;    



   public ListNode getKthLastElement(int k){
    var left = head;
    var right = head.next.next;

    while(right.next != null){
      
    }

    return left;
 
   } 
}
