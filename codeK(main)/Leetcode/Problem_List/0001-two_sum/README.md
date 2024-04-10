# Leetcode - Two Sum

## Problem Description

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`.

You may assume that each input would have **exactly one solution**, and you may not use the same element twice.

You can return the answer in any order.

## Solution

The solution to this problem is implemented in the Python code. Here's how it works:


The goal is to find two numbers in the `nums` list that add up to the `target` value. We can do this by using a dictionary to keep track of the numbers we've seen so far and their positions in the list.

Here's how it works:
1. We start by creating an empty dictionary called `complement_dict`.
2. We then loop through the `nums` list. For each number `num`, we calculate the `complement`, which is the number that needs to be added to `num` to get the `target`.
3. We check if the `complement` is already in the `complement_dict`. If it is, that means we've found the two numbers that add up to the `target`, so we return their indices.
4. If the `complement` is not in the `complement_dict`, we add the current `num` and its index `i` to the `complement_dict`.
5. If we finish looping through the entire `nums` list without finding a solution, we return an empty list.

The key ideas are:
- Use a dictionary to keep track of the numbers we've seen and their positions
- Calculate the "complement" for each number and check if it's in the dictionary
- If the complement is found, return the indices of the two numbers
- If no solution is found, return an empty list

Does this make sense? Great!

## Usage

To use the solution, you can call the `twoSum` method with an integer array and a target integer:

```python
nums = [2, 7, 11, 15]
target = 9
solution = Solution()
indices = solution.twoSum(nums, target)
print(indices)  # Output: [0, 1]
```

## Complexity Analysis

- **Time Complexity:** O(n), where n is the length of the input array `nums`. This is because we are iterating through the array once, and the lookup in the dictionary is constant time.
- **Space Complexity:** O(n), where n is the length of the input array `nums`. This is because we are storing each number and its index in the `complement_dict` dictionary.
