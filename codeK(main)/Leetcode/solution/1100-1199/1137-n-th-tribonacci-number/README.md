# Leetcode - Tribonacci Number

## Problem Description

The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

## Solution

To solve this problem, we can use a simple iterative approach where we calculate each term of the Tribonacci sequence iteratively based on the previous three terms. We start with the initial conditions T0 = 0, T1 = 1, and T2 = 1, and then calculate the subsequent terms until we reach the desired term Tn.

Here's how we can approach this problem:

1. Initialize variables `a`, `b`, and `c` to represent the first three terms of the Tribonacci sequence: `T0 = 0`, `T1 = 1`, and `T2 = 1`, respectively.
2. Iterate `n` times, starting from 3, to calculate the next term of the Tribonacci sequence using the formula `Tn = a + b + c`.
3. Update the variables `a`, `b`, and `c` accordingly to prepare for the next iteration.
4. After `n` iterations, return the value of `c`, which represents the `n-th` term of the Tribonacci sequence.

By iteratively calculating the terms of the Tribonacci sequence, we can efficiently find the value of Tn.

## Usage

To use the solution, create an instance of the `Solution` class and call the `tribonacci` method with the input parameter `n`:

```python
solution = Solution()
# Define the value of n
# n = 4
# Call the tribonacci method
result = solution.tribonacci(n)
print(result)
```

```python
# n = 4
```

[Link to detailed explanation](https://tecadmin.net/what-is-fibonacci-sequence/)


[Link to detailed explanation on Medium](https://tarunjain07.medium.com/fibonacci-sequence-complexity-analysis-notes-1fbd529a8b9d)


[Link to detailed explanation on Geeksforgeeks](https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/)


[Link to detailed explanation on Medium](https://medium.com/@trejonstallsworth/fibonacci-recursion-memoization-b7ce6e50c3ee)






## Check Out this video

[![Video Explanation](https://img.youtube.com/vi/pqivnzmSbq4/mqdefault.jpg)](https://youtu.be/pqivnzmSbq4)


[![Video Explanation](https://img.youtube.com/vi/3lpNp5Ojvrw/mqdefault.jpg)](https://youtu.be/3lpNp5Ojvrw)


[![Video Explanation](https://img.youtube.com/vi/SilT6i1DEe8/mqdefault.jpg)](https://youtu.be/SilT6i1DEe8)


## Complexity Analysis

- **Time Complexity:** O(N), where N is the input parameter `n`. We iterate `n` times to calculate the `n-th` term of the Tribonacci sequence.
- **Space Complexity:** O(1), excluding the space required for input and output. We use only a constant amount of extra space for storing the variables `a`, `b`, and `c`.