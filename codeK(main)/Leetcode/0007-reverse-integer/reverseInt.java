public class reverseInt {
    public int reverse (int x) {
        int rev = 0;

        while(x != 0) {
            int digit = x % 10; //gets the last digit of the int
            rev = (rev * 10) + digit; //reverses the last digit
            x = x / 10; //goes to the next digit 
        }

        return rev;
    }
}
