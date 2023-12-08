
public class reverseInt {
    public static void main(String[] args) {
        System.out.println(reverse(987654321)); //test
    }
    public static int reverse(int x) {
        int rev = 0;

        while(x != 0) {
            int digit = x % 10; //gets the last digit of the int
            rev = (rev * 10) + digit; //reverses the last digit
            x /= 10; //goes to the next digit 

            if(rev > Integer.MAX_VALUE/10 || rev < Integer.MIN_VALUE/10){ //signed 32-bit integer range [-2^32 , 2^32 - 1]
                return 0;
            }
        }

        return rev;
    }

    class Solution {// Leetcode solution
        public int reverse(int x) {
          long ans = 0;
      
          while (x != 0) {
            ans = ans * 10 + x % 10;
            x /= 10;
          }
      
          return (ans < Integer.MIN_VALUE || ans > Integer.MAX_VALUE) ? 0 : (int) ans;
        }
      }
}
