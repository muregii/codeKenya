public class reverseInt {
    public int reverse (int x) {
        int rev = 0;

        while(x != 0) {
            int digit = x % 10;
            rev = (rev * 10) + digit;
            x = x / 10;
        }

        return rev;
    }
}
