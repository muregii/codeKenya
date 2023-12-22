public class SortedListRemoval {
  public ListNode uniqify(ListNode list){
      ListNode first = list;
      ListNode prev = first;
      ListNode current = first;

    while(current != null ) {
          if (current.info == prev.info){
              prev = current.next;
          }
          current = current.next;
    }

    return list;

  }
}