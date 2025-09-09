/* Solve the questions below using java
   There are N balls positioned in a row. Each of them is either red (R) or white (W). In one move we can swap two adjacent balls. 
   We want to arrange all the red balls into a consistent segment. What is the minimum number of swaps needed?

   Write a function:

   function solution(S: string): number;

   that, given a string S of length N, built from characters "R" and "W", representing red and white balls respectively, 
   returns the minimum number of swaps needed to arrange all the red balls into a consistent segment. 
   If the result exceeds 1,000,000,000, return -1.
*/

import java.util.*;

public class codilityQ1 {

    public static int Solution(String s) { // WRRWRW 012345
        ArrayList<Integer> reds = new ArrayList<>(); //declare an ArrayList for the red balls
        for(int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == 'R') {
                reds.add(i); //124 -> 012  4-1-2+0
            }
        }

        int n = reds.size(); //n is the size of the ArrayList or rather number of red balls
        int startPtr = 0; //pointer to the beginning of the first index of the string ->WRWWWRR...
        int endPtr = n - 1; //pointer to the last index of R in the string ...rWRR<-WW
        long count = 0; // Use long to avoid overflow

        if (n == 0 || n == s.length()) { // No 'R's or all 'R' in the string means no swaps needed
            return 0;
        }
        // logic to calculate minimum swaps
        while (startPtr < endPtr) {
            count += reds.get(endPtr) - reds.get(startPtr) - endPtr + startPtr; //4-1-2+0 WRWWWRR 0123456 5-1-;
            startPtr++;
            endPtr--;
        }

        if (count > 1000000000) {
            return -1;
        }

        return (int) count; // Cast count to int from long before returning
        
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the string:");
        String s = scanner.nextLine();
        int result = Solution(s);
        System.out.println(result);
    }
}

//Time Complexity == O(n)