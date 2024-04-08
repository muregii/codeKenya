# Leetcode - Reverse Integer

Okay, let's explain the code and my thought process.
Imagine you have a number, like 987654321. What if we wanted to reverse the order of the digits in that number? That means we'd want to change it to 123456789.

To do this in coding, we can use a few simple steps:

1. We start with the original number, 987654321.
2. We look at the last digit, which is 1. We're going to add that 1 to a new number we're building, called 'rev'.
3. Then we look at the next digit, which is 2. We add that to 'rev', making it 21.
4. We keep doing this, taking the last digit of the original number and adding it to 'rev', until we've gone through all  the digits.
5. But we have to be careful, because if the new number gets too big or too small, it won't fit in the computer's memory. So we check for that and return 0 if it doesn't fit.

The code has two methods for reversing an integer:

1. The first method uses an int variable rev to build up the reversed number. It does this by repeatedly taking the last digit of the original number, adding it to rev, and then moving to the next digit. It checks if the reversed number would overflow the 32-bit integer range and returns 0 if so.

2. The second method, from the Leetcode solution, is similar but uses a long variable ans instead of an int. This is to prevent overflow issues, as the reversed number may exceed the 32-bit integer range during the intermediate calculations.

Both methods return the reversed number if it fits within the 32-bit signed integer range, or 0 if it doesn't.

## Problem Description

Given a signed 32-bit integer `x`, return `x` with its digits reversed. If reversing `x` causes the value to go outside the signed 32-bit integer range `[-2^31, 2^31 - 1]`, then return `0`.

## Solution

The solution to this problem is implemented in the file `reverseInt.java`. The key steps are:

1. Initialize a `rev` variable to store the reversed integer.
2. Iterate through the digits of the input integer `x`:
   - Get the last digit of `x` using the modulo operator `%`.
   - Append the last digit to the `rev` variable by multiplying `rev` by 10 and adding the digit.
   - Move to the next digit of `x` by integer division (`/=`) by 10.
3. Check if the reversed integer `rev` is within the signed 32-bit integer range `[-2^31, 2^31 - 1]`. If not, return 0.
4. Return the reversed integer `rev`.

The provided solution also includes a `Solution` class that implements the same logic, but with the use of a `long` variable `ans` to handle the intermediate calculations before casting the final result to an `int`.

## Usage

To use the solution, you can call the `reverse` method with an integer argument:

```java
public static void main(String[] args) {
    System.out.println(reverse(987654321)); // Output: 123456789
}
```

## Complexity Analysis

- **Time Complexity:** O(log n), where n is the absolute value of the input integer. This is because we are iterating through the digits of the integer, and the number of digits is proportional to the logarithm of the integer.
- **Space Complexity:** O(1), as we are only using a constant amount of extra space to store the reversed integer.
