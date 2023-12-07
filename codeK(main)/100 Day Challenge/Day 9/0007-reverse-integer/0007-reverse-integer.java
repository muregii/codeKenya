class Solution {
  public static int reverse(int x) {
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
}

// # This passes all test cases, including the -2^32, 2^32 -1 range constraint.