class Palindrome {
    public static void main(String[] args) {
        boolean result = isPalindrome(12121);
        System.out.println(result);
    }

    public static boolean isPalindrome(int x) {
        int temp = x ,rev = 0;
        
        while(x > 0){
            int digit = x % 10;
            rev = rev * 10 + digit; 
            x = x / 10;
        }
        if(rev == temp){
            return true;
        }else{
            return false;
        }
    }
}