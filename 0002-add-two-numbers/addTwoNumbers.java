/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public class ListNode {
      int val;
      ListNode next;
      ListNode() {}
      ListNode(int val) { this.val = val; }
      ListNode(int val, ListNode next) { this.val = val; this.next = next; }
  }
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode tempHead = new ListNode(0);
        ListNode list1 = l1, list2 = l2, current = tempHead;
        int numberCarried = 0;

        while(list1 != null || list2 != null){
            int x, y;
            if(list1 != null){
                x = list1.val;
            }
            else{
                x = 0;
            }

            if(list2 != null){
                y = list2.val;
            }
            else{
                y = 0;
            }

            
            int sum = x + y + numberCarried;
            numberCarried = sum/10;
            current.next = new ListNode(sum % 10);
            current = current.next;

            if(list1 != null) list1 = list1.next;
            if(list2 != null) list2 = list2.next;

        }

        if(numberCarried > 0){
            current.next = new ListNode(numberCarried);
        }

        return tempHead.next; 
    }
}










