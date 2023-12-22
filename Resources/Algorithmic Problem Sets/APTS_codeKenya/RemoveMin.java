
public class RemoveMin {
    public ListNode remove (ListNode list) {
    // replace statement below with code you write..
    if(list == null || list.next == null) {
        return null;
    } 
    
    
    ListNode temp = new ListNode(0, list);
   
    ListNode prev = null;
    ListNode next = null;
    ListNode last = null;
    int val = 1111;
    while(list != null){
        if(val > list.info){
            prev = last;
            next = list.next;
            val = list.info;
        }
        last = list;
        list = list.next;
        }

        
        if(prev == null){
            return next;
        }
        else if(next == null) {
            prev.next = null;
        }
        else{
            prev.next = next;
        }
        return temp.next;

    }


}

