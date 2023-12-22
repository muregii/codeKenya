
//reverse A B C to C B A
public static main{
    public ListNode reverse(Listnode front);

}
public ListNode reverse(Listnode front) {
    ListNode rev = null;
    Listnode list = front;
    while (list!= null) {
        //operations
    Listnode temp = list.next;
    list.next = rev;
    rev = list;
    list = temp;
    }
    return rev;

}


