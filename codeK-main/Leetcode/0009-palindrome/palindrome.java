class Palindrome {
    public static void main(String[] args) {
        boolean result = isPalindrome(123);
        System.out.println(result);
    }

    public static boolean isPalindrome(int x) {
        int temp=x ,rev = 0;
        if (x < 0) return false;
        while(x > 0){
            int digit = x % 10;
            rev = rev * 10 + digit; 
            x = x / 10;
        }
        if(temp == x){
            return true;
        }else{
            return false;
        }
    }
}