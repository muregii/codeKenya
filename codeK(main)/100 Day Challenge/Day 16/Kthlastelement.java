
public class KthLastElement {
   
    public class ListNode{
       
      private ListNode next;
      private int info;
       

      public ListNode(int info) {
         
         this.info = info;
      }
   } 
   private ListNode head;
  
   //private int size;    

   // 10 -> 20 -> 30 -> 40
   //  *                 *
   public int getKthLastElement(int k){
      if(head == null || k < 0) return -1;

    var left = head;
    var right = head;
   
    for(int i = 0; i < k - 1; i++){
      if(right.next == null) return -1;
      right = right.next;
      
    }

    while(right.next != null){
      left = left.next;
      right = right.next;

    }
   

    return left.info;
 
   } 
}
