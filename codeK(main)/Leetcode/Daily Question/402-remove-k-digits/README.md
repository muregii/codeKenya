# Leetcode - Remove K Digits

## Problem Description

Given a string `num` representing a non-negative integer, and an integer `k`, return the smallest possible integer 
after removing `k` digits from `num`.


## Solution

"Alright, imagine you have a string of numbers written down. Now, you want to remove some of these numbers to make the smallest possible number.

Here's how we can do it:

1. We start by looking at the digits from left to right.
2. If we find a digit that is greater than the digit to its right, we remove that digit. This ensures that the remaining number is as small as possible.
3. We repeat this process `k` times, removing `k` digits in total.
4. After removing `k` digits, we'll have the smallest possible number remaining.

For example, if our number is '1432219' and `k` is 3, we'll remove the digits '4', '3', and '9' to get the smallest number '1221'.

Does this make sense? Great!

## Usage

To use the solution, simply create an instance of the `Solution` class and call the `removeKdigits` method with the input string `num` and the integer `k`:

```python
solution = Solution()
result = solution.removeKdigits(num, k)
print(result)
```

This will output the smallest possible integer after removing `k` digits from `num`.

[Link to detailed explanation on Medium](https://medium.com/@mistysamia/402-remove-k-digits-leetcode-83b09be3dbf1)


## Check Out this videos

[![Video Explanation](https://img.youtube.com/vi/3QJzHqNAEXs/0.jpg)](https://youtu.be/3QJzHqNAEXs)


[![Video Explanation](https://img.youtube.com/vi/cFabMOnJaq0/0.jpg)](https://youtu.be/cFabMOnJaq0)

The videos above explain the solution approach in detail.


## Complexity Analysis

- **Time Complexity:** O(n), where n is the length of the input string `num`.
- **Space Complexity:** O(n), as we use a stack to store the digits of the input number.

---