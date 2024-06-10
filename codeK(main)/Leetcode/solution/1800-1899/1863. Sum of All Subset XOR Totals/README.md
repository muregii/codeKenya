# Leetcode - Sum of All XOR Totals for Every Subset

## Problem Description

The **XOR total** of an array is defined as the bitwise `XOR` of **all its elements**, or `0` if the array is **empty**. 
- For example, the **XOR total** of the array `[2, 5, 6]` is `2 XOR 5 XOR 6 = 1`.

Given an array `nums`, *return the **sum** of all **XOR totals** for every subset of* `nums`.

Note: Subsets with the **same** elements should be counted **multiple** times.

An array `a` is a **subset** of an array `b` if `a` can be obtained from `b` by deleting some (possibly zero) elements of `b`.

**Constraints:**
- `1 <= nums.length <= 12`
- `1 <= nums[i] <= 20`

## Solution

Calculate the XOR total for every subset of the given array `nums` and sum them up.

Say you have a bag of numbers. You want to find out how many different ways you can pick some numbers from the bag and then do a special math trick called XOR on them. XOR is like a magic operation that changes numbers in a special way. We want to do this for every possible group of numbers we can pick from the bag and then add up all the results.


The `subsetXORSum` method takes an array `nums` and returns the sum of all XOR totals for every subset of `nums`.

1. **Understanding XOR Operation:**
   - The XOR operation is a bitwise operation that changes bits based on whether they are the same or different. For example, `2 XOR 5` changes the bits of `2` and `5` to give a new number.
   
2. **Generating Subsets:**
   - We can generate all possible subsets of the array using a recursive approach.
   - For each subset, calculate the XOR total and add it to the sum.

3. **Algorithm:**
   - Use a helper function to recursively generate subsets and calculate the XOR total for each subset.
   - Sum up all the XOR totals.


```python

class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
```

## Usage

To use the solution, create an instance of the `Solution` class and call the `subsetXORSum` method with the array `nums`:

```python
solution = Solution()
nums = [2, 5, 6]
result = solution.subsetXORSum(nums)
print(result)  # Output: 28
```

[Link to detailed explanation on AlgoMonster](https://algo.monster/liteproblems/1863)

[Link to detailed explanation on Medium](https://csmonks.com/sum-of-all-subset-xor-totals-928a06fb7ae0)

[Link to detailed explanation on Geeksforgeeks](https://www.geeksforgeeks.org/sum-xor-possible-subsets/)

[Link to detailed explanation on Quora](https://www.quora.com/How-do-I-calculate-all-the-possible-XOR-values-of-all-subsets-of-an-array)

## Check Out this videos

[![Video Explanation](https://img.youtube.com/vi/LI7YR-bwNYY/mqdefault.jpg)](https://youtu.be/LI7YR-bwNYY)

[![Video Explanation](https://img.youtube.com/vi/_YdRjA5EvK4/mqdefault.jpg)](https://youtu.be/_YdRjA5EvK4)

[![Video Explanation](https://img.youtube.com/vi/YxtxNmhiXro/mqdefault.jpg)](https://youtu.be/YxtxNmhiXro)

## Complexity Analysis

- **Time Complexity:** O(2^n), where n is the length of the array `nums`. This is because we are generating all possible subsets.
- **Space Complexity:** O(n), where n is the length of the array `nums`. This is the space used by the recursion stack.