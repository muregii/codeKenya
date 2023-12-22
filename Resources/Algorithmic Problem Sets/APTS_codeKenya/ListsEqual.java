
public class ListsEqual {
    public int equal (ListNode a1, ListNode a2) {
    // replace statement below with code you write.
    ListNode temp1 = a1;
    ListNode temp2 = a2;
    int count1 = 0;
    int count2= 0;
    while(temp1 != null) {
        count1++;
        temp1 = temp1.next;
    }
    

    while(temp2 != null) {
        count2++;
        temp2 = temp2.next;
    }
    if(count1 != count2){
        return 0;
    }

    while(a1 != null && a2 != null){
        
        if(a1.info != a2.info){
        return 0;
        }
        a1 = a1.next;
        a2 = a2.next;
 
    }
    return 1;
}
}