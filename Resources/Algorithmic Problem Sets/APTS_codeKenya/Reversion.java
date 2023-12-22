public class Reversion {
    public ListNode reverseFrom(ListNode list, int start) {
        if (list == null || start < 0) {
            return list;
        }

        ListNode prev = null;
        ListNode current = list;
        int index = 0;

        while (index < start && current != null) {
            prev = current;
            current = current.next;
            index++;
        }

        if (current == null) {
            return list;
        }

        ListNode lastReversed = prev;
        ListNode firstNodeInReversedPart = current;
        ListNode next;

        while (current != null) {
            next = current.next;
            current.next = prev;
            prev = current;
            current = next;
        }

        if (lastReversed != null) {
            lastReversed.next = prev;
        } else {
            list = prev;
        }

        firstNodeInReversedPart.next = current;

        return list;
    }
}