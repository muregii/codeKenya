public class DIYLinkedList {
    
    private class ListNode {
        int value;
        ListNode next;
        public ListNode(int value){
            this.value =  value;
        }
        public ListNode (int value, ListNode next){
            this.value = value;
            this.next = next;
        }
    }

    int value;
    String next;
    private ListNode current;
    private int size;
    private ListNode first;
    private ListNode last;

    public class DIYLinkedList {
        return size;
    }
        
    

    public int size() {
        return size;
    }

    public void add(int element) {
        if(last == null) {
            last = new ListNode(element);
            first = last;
        }
        else{
        last.next = new ListNode(element);
        last = last.next;

        }

        size++;

    }

    public int get(int index) {
        if(index < 0 || index >= size) {
            throw new IndexOutOfBoundException("Invalid Index");
        }
        current = first;
        for(int i=0;i<index;i++) {
            current = current.next;
        }
        return current.value;
    }


}

