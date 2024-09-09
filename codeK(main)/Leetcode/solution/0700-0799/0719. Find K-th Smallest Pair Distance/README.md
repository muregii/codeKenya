# Leetcode - Find K-th Smallest Pair Distance

## Problem Description

The **distance** of a pair of integers `a` and `b` is defined as the absolute difference between `a` and `b`.

Given an integer array `nums` and an integer `k`, return the `kth` smallest ***distance among all the pairs nums[i] and nums[j] where** 0 <= i < j < nums.length.
*

**Constraints:**
- `n == nums.length`
- `2 <= n <= 10^4`
- `0 <= nums[i] <= 10^6`
- `1 <= k <= n * (n - 1) / 2`

## Solution

**Understanding the Problem:**
   - We need to find the `k`th smallest distance among all pairs in the `nums` array.
   - A **distance** between two numbers is defined as the absolute difference.
   - There can be many pairs, and we need an efficient way to find the `k`th smallest without generating all pairs.

**Breaking It Down**
   - **Binary Search on Distance:**
     - The problem asks for the `k`th smallest distance, so we can think about using **binary search** over the possible distances.
     - The smallest distance is `0` (if there are duplicate numbers in the array), and the largest distance is `max(nums) - min(nums)`.
     
   - **Counting Pairs with Distance Less Than or Equal to Mid:**
     - For each mid-point in our binary search, we count how many pairs have a distance less than or equal to `mid`. This is done using a two-pointer approach.
     - If the count of such pairs is greater than or equal to `k`, we reduce our search range; otherwise, we increase it.
     
   - **Two-pointer Approach to Count Pairs:**
     - First, we sort the array. For each number at position `i`, we use a second pointer `j` to find how many numbers have a difference of less than or equal to `mid`.

**Implementation Approach:**
   - **Binary Search:** Perform a binary search on the possible range of distances.
   - **Two-pointer Count:** For each midpoint in the binary search, count the number of pairs with a distance less than or equal to `mid`.
   - **Adjust Search Range:** Adjust the binary search range based on whether the count of valid pairs is greater or less than `k`.

**Algorithm Steps:**
   - **Sort the Array:** Sort the input array to facilitate the two-pointer approach.
   - **Binary Search:** Use binary search to find the `k`th smallest distance.
   - **Count Pairs:** For each midpoint, count the number of pairs with a distance less than or equal to `mid` using two pointers.
   - **Adjust Range:** If the count is greater than or equal to `k`, search in the lower half; otherwise, search in the upper half.

### Python Code

```python
class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Example

```python
# Input
nums = [1, 3, 1]
k = 1

# Output
0
```

### Explanation

1. **Initial Array:** `[1, 1, 3]` after sorting.
2. **Possible Pair Distances:** The possible pair distances are `|1 - 1| = 0`, `|1 - 3| = 2`, `|1 - 3| = 2`. 
3. **Result:** The 1st smallest distance is `0`.

### Usage

To use the solution, create an instance of the `Solution` class and call the `smallestDistancePair` method with the `nums` array and `k`:

```python
# Example usage
solution = Solution()
nums = [1, 3, 1]
k = 1
result = solution.smallestDistancePair(nums, k)
print(result)  # Output: 0
```

### Additional Resources

[Link to detailed explanation on Algo Monster](https://algo.monster/liteproblems/719)

[Link to detailed explanation on Medium](https://medium.com/swlh/binary-search-find-k-th-smallest-pair-distance-91cce923c273)

[Link to detailed explanation on Geeksforgeeks](https://www.geeksforgeeks.org/k-th-smallest-absolute-difference-two-elements-array/)


### Check Out These Video(s)

[![Video Explanation](https://img.youtube.com/vi/ZXpYPeRE66E/mqdefault.jpg)](https://youtu.be/ZXpYPeRE66E)

[![Video Explanation](https://img.youtube.com/vi/bQ-QcFKwsZc/mqdefault.jpg)](https://youtu.be/bQ-QcFKwsZc)

[![Video Explanation](https://img.youtube.com/vi/ym93rTBR4j8/mqdefault.jpg)](https://youtu.be/ym93rTBR4j8)


### Complexity Analysis

- **Time Complexity:** O(n log n + n log d), where `n` is the length of the array and `d` is the maximum difference between numbers. Sorting the array takes `O(n log n)` and binary searching for the result involves O(n log d).
- **Space Complexity:** O(1), for using a constant amount of additional space beyond the input array.