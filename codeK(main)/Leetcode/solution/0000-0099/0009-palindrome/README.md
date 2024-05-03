# Leetcode - Palindrome Number

## Problem Description

Given an integer `x`, return `true` if `x` is a palindrome, and `false` otherwise.

A palindrome is a number or a word that reads the same backward as forward.

## Solution

The solution to this problem is implemented in the file `Palindrome.java`. Here's how it works:

### Explanation

The goal is to check if a number is a palindrome, meaning it reads the same forward and backward. For example, 12121 is a palindrome, but 12345 is not.

To do this, we first save the original number in a variable called `temp`. Then, we start building a new number called `rev` by taking the last digit of the original number, adding it to `rev`, and then moving on to the next digit.

We keep doing this until we've gone through all the digits. At the end, we compare the final `rev` number to the original `temp` number. If they are the same, then the original number is a palindrome, and we return `true`. If they are different, we return `false`.

The key steps are:
1. Save the original number in `temp`
2. Initialize `rev` to 0
3. Loop through the digits, adding them to `rev`
4. Compare `rev` to `temp` and return `true` if they are equal, `false` otherwise

Does this make sense? Great!

## Usage

To use the solution, you can call the `isPalindrome` method with an integer argument:

```java
public static void main(String[] args) {
    boolean result = isPalindrome(12121);
    System.out.println(result); // Output: true
}
```

## Complexity Analysis

- **Time Complexity:** O(log n), where n is the input integer. This is because we are iterating through the digits of the integer, and the number of digits is proportional to the logarithm of the integer.
- **Space Complexity:** O(1), as we are only using a constant amount of extra space to store the `temp` and `rev` variables.