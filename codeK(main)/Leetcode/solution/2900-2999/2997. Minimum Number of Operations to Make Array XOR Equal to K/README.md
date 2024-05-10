# Leetcode - Minimum Operations to Make XOR of Array Equal to K

## Problem Description

You are given a **0-indexed integer** array `nums` and a positive integer `k`.

You can apply the following operation on the array any number of times:

Choose any element of the array and flip a bit in its **binary** representation. Flipping a bit means changing a 0 to 1 or vice versa.

Return *the minimum number of operations required to make the bitwise `XOR` of all elements of the final array equal to `k`.* 

Note that you can flip leading zero bits in the binary representation of elements. For example, for the number `(101)₂` you can flip the fourth bit and obtain `(1101)₂`.

## Solution

To solve this problem, we can iterate through the binary representation of `k` from left to right and count the number of operations required to match each bit.

Here's how we can approach this problem:

1. Convert `k` to binary representation.
2. Iterate through each bit of the binary representation of `k` from left to right.
3. For each bit position, count the number of set bits in `nums` and calculate the number of operations required to match the current bit with the corresponding bit in `k`.
4. Sum up the number of operations required for all bit positions.
5. The total sum represents the minimum number of operations required to make the bitwise XOR of all elements of the final array equal to `k`.

## Usage

To use the solution, create an instance of the `Solution` class and call the `minOperations` method with the input parameters `nums` and `k`:

```python
solution = Solution()
# Define the input array nums and the target integer k
# nums = [1, 2, 3, 4, 5]
# k = 4
# Call the minOperations method
result = solution.minOperations(nums, k)
print(result)
```

```python
# nums = [1, 2, 3, 4, 5]
# k = 4
```

[Link to detailed explanation on Geeksforgeeks](https://www.geeksforgeeks.org/maximum-xor-of-two-numbers-in-an-array/)


[Link to detailed explanation on Medium](https://medium.com/@kapoorprakhar99/maximum-xor-of-two-numbers-11efa24b2fcc)

[Link to detailed explanation on Geeksforgeeks](https://www.geeksforgeeks.org/check-if-it-is-possible-to-construct-an-array-of-size-n-having-sum-as-s-and-xor-value-as-x/)

## Check Out this video

[![Video Explanation](https://img.youtube.com/vi/QZuWyxX3vv8/mqdefault.jpg)](https://youtu.be/QZuWyxX3vv8)

## Complexity Analysis

- **Time Complexity:** O(n * log(max(nums))), where n is the number of elements in `nums` and `max(nums)` is the maximum element in `nums`. We iterate through the binary representation of `k` and count the set bits for each element in `nums`.
- **Space Complexity:** O(1). We use only constant extra space for storing intermediate results.