# Leetcode - Subarray Sums Divisible by K

## Problem Description

Given an integer array `nums` and an integer `k`, *return the number of non-empty subarrays that have a sum divisible by `k`.*

A **subarray** is a **contiguous** part of an array.

**Constraints:**
- `1 <= nums.length <= 3 * 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `2 <= k <= 10^4`

## Solution

To determine the number of subarrays in `nums` that have a sum divisible by `k`, use the concept of **prefix sums** and **modulo operations**. This allows us to efficiently count the subarrays without having to check every possible subarray individually.

### Step-by-Step Explanation

1. **Understanding Prefix Sums:**
   - A **prefix sum** is the cumulative sum of elements from the start of the array up to a given index. For example, for an array `[1, 2, 3]`, the prefix sums are `[1, 3, 6]`.

2. **Modulo Operation:**
   - By computing the modulo `k` of each prefix sum, we can determine if the sum of a subarray is divisible by `k`. If the difference between two prefix sums is a multiple of `k`, then the subarray sum between these two points is divisible by `k`.

3. **Using a HashMap for Remainders:**
   - We use a hashmap (or dictionary) to track how many times each remainder has occurred.
   - If the same remainder occurs more than once, it means that the subarray between these occurrences has a sum that is divisible by `k`.

4. **Counting Subarrays:**
   - As we traverse the array and compute prefix sums and their remainders, we use the hashmap to count how many times each remainder has appeared. This helps us count the number of subarrays with sums divisible by `k`.

### Example

Imagine you have a list of numbers `[4, 5, 0, -2, -3, 1]` and `k = 5`. You want to find out how many subarrays have a sum that is divisible by `5`.

1. Compute prefix sums: `[4, 9, 9, 7, 4, 5]`
2. Compute remainders: `[4, 4, 4, 2, 4, 0]`
3. Use a hashmap to count occurrences of remainders. For example, remainder `4` appears multiple times, indicating multiple subarrays whose sum is divisible by `5`.

### Python Code

```python
class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Usage

To use the solution, create an instance of the `Solution` class and call the `subarraysDivByK` method with the array of numbers (`nums`) and the integer `k`:

```python
solution = Solution()
nums = [4, 5, 0, -2, -3, 1]
k = 5
result = solution.subarraysDivByK(nums, k)
print(result)  # Output: 7, because there are 7 subarrays with sums divisible by 5.
```

### Additional Resources

[Link to detailed explanation on GeeksforGeeks](https://www.geeksforgeeks.org/longest-subarray-sum-divisible-k/)

[Link to detailed explanation on Medium](https://medium.com/@sheefanaaz6417/974-subarray-sums-divisible-by-k-step-by-step-approach-a7117646acc5)

[Link to detailed explanation on AlgoMonster](https://algo.monster/liteproblems/974)

### Check Out These Videos

[![Video Explanation](https://img.youtube.com/vi/bcXy-T4Sc3E/mqdefault.jpg)](https://youtu.be/bcXy-T4Sc3E)

[![Video Explanation](https://img.youtube.com/vi/C0okNE_tt14/mqdefault.jpg)](https://youtu.be/C0okNE_tt14)

[![Video Explanation](https://img.youtube.com/vi/u9m-hnlcydk/mqdefault.jpg)](https://youtu.be/u9m-hnlcydk)

### Complexity Analysis

- **Time Complexity:** O(n), where `n` is the number of elements in `nums`. We iterate through the array once, making the algorithm linear in time complexity.
- **Space Complexity:** O(k), where `k` is the number of possible remainders. In the worst case, we store up to `k` remainders in the hashmap.