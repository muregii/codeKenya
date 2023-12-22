
public class ListSum {
    public int sum(ListNode list, int thresh) {
        // replace statement below with code you write
        int sum = 0;
        while(list != null) {
          if(list.info > thresh){
            sum+=list.info;
          } 
          list = list.next;
        }

        return sum;
}
public static void main(String[] args)  {


  }
}



