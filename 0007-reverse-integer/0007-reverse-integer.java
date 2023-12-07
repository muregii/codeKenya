class Solution {
  public static int reverse(int x) {
      int PLACE_VALUE_10 = 10;
      
      long rev = 0;
      
      while( x != 0) {
          //1234
          int digit = x % PLACE_VALUE_10;
          rev = (rev * 10) + digit; // 4 -> 43 -> 432 -> 4321
          x /= PLACE_VALUE_10;
          if(rev > Integer.MAX_VALUE || rev < Integer.MIN_VALUE){
              return 0;
          }
      } 
      return (int) rev;
 }
}