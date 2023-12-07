import java.util.*;
import java.util.LinkedList;

class Solution {
  public static int reverse(int x) { //1 ms runtime (Beats 97.54 % of Java users) Beats only 7.73% of Java users in memory efficiency.
      int PLACE_VALUE_10 = 10; 

      long rev = 0; 
      while( x != 0) {
        
          int digit = x % PLACE_VALUE_10; 
          rev = (rev * 10) + digit;
          x /= PLACE_VALUE_10; 

          if(rev > Integer.MAX_VALUE || rev < Integer.MIN_VALUE){
              return 0;
          }
      } 
      return (int) rev; 
    }

    public static int reverse1(int x) { //2 ms(beats 16.60 %) Beats only 7.76 % of Java Users in memory efficiency.
      int  PLACE_VALUE_10 = 10;

      Deque<Integer> deq = new ArrayDeque<>();
      
      while (x != 0){
          deq.add(x % 10);
          x /= 10;
      }
      long rev = 0;
      while(!deq.isEmpty()) {
          //1234
          rev = (rev * PLACE_VALUE_10) + deq.removeFirst();
          
          if(rev > Integer.MAX_VALUE || rev < Integer.MIN_VALUE){
              return 0;
          }
      } 
      return (int) rev;
    }

    public static int reverse2(int x) { //2 ms runtime(Beats 16.60%) Beats 37% Java users in memory efficiency.
      int  PLACE_VALUE_10 = 10;

      Queue<Integer> Q = new LinkedList<>();
      
      while (x != 0){
          Q.add(x % 10);
          x /= 10;
      }
      long rev = 0;
      while(!Q.isEmpty()) {
          //1234
          rev = (rev * PLACE_VALUE_10) + Q.remove();
          
          if(rev > Integer.MAX_VALUE || rev < Integer.MIN_VALUE){
              return 0;
          }
      } 
      return (int) rev;
 }
}

// # This passes all test cases, including the -2^32, 2^32 -1 range constraint.