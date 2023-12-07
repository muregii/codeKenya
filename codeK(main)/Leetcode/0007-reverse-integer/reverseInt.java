
public class reverseInt {
    public static void main(String[] args) {
        System.out.println(reverse(987654321)); //test
    }
    public static int reverse (int x) {
        int rev = 0;

        while(x != 0) {
            int digit = x % 10; //gets the last digit of the int
            rev = (rev * 10) + digit; //reverses the last digit
            x /= 10; //goes to the next digit 
        }

        return rev;
    }
}
