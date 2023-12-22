public class MergeLists {
public ListNode weave(ListNode a, ListNode b) {
    ListNode result = new ListNode(0);
    ListNode curr = result;
    while (a != null && b != null) {
        curr.next = a;
        a = a.next;
        curr = curr.next;
        curr.next = b;
        b = b.next;
        curr = curr.next;
    }
    return result.next;
}
}
