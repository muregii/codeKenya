# Leetcode - Minimum Number of Days to Make m Bouquets

## Problem Description

You are given an integer array `bloomDay`, an integer `m`, and an integer `k`.

You want to make `m` bouquets. To make a bouquet, you need to use `k` **adjacent flowers** from the garden.

The garden consists of `n` flowers, the `ith` flower will bloom in the `bloomDay[i]` and then can be used in **exactly one** bouquet.

*Return the minimum number of days you need to wait to be able to make `m` bouquets from the garden. If it is impossible to make `m` bouquets, return `-1`.*

**Constraints:**
- `bloomDay.length == n`
- `1 <= n <= 10^5`
- `1 <= bloomDay[i] <= 10^9`
- `1 <= m <= 10^6`
- `1 <= k <= n`

## Solution

To determine the minimum number of days needed to make `m` bouquets, use a binary search approach on the number of days.

1. **Understanding the Problem:**
   - Find the minimum days required such that we can form `m` bouquets with each bouquet consisting of `k` adjacent flowers.
   - Each flower blooms on a specific day given in the `bloomDay` array.
   - If it's not possible to make `m` bouquets, we return `-1`.

2. **Using a Binary Search Approach:**
   - Use binary search to find the minimum number of days.
   - For each mid value in the binary search, check if it's possible to make `m` bouquets within `mid` days.

3. **Algorithm Steps:**
   - Initialize `left` to 1 (minimum day) and `right` to the maximum value in `bloomDay` (maximum day).
   - Perform binary search:
     - Calculate `mid`.
     - Check if `mid` days are enough to make `m` bouquets using a helper function.
     - Adjust `left` and `right` based on the result of the helper function.
   - If `left` exceeds `right`, return `-1`.

### Example

Suppose you have `bloomDay = [1, 10, 3, 10, 2]`, `m = 3`, and `k = 1`.

1. Initialize `left = 1` and `right = 10` (maximum value in `bloomDay`).
2. Perform binary search:
   - Check if it’s possible to make `3` bouquets in `5` days:
     - Bloomed flowers in 5 days: `[1, 3, 2]`.
     - Possible to make `3` bouquets.
   - Adjust `right` to `5`.
3. Check if it’s possible to make `3` bouquets in `3` days:
   - Bloomed flowers in 3 days: `[1, 3, 2]`.
   - Possible to make `3` bouquets.
   - Adjust `right` to `3`.
4. Check if it’s possible to make `3` bouquets in `2` days:
   - Bloomed flowers in 2 days: `[1, 2]`.
   - Not possible to make `3` bouquets.
   - Adjust `left` to `3`.

The minimum number of days to make `3` bouquets is `3`.

### Python Code


```python
class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
       
```

### Usage

To use the solution, create an instance of the `Solution` class and call the `minDays` method with `bloomDay`, `m`, and `k`:

```python
solution = Solution()
bloomDay = [1, 10, 3, 10, 2]
m = 3
k = 1
result = solution.minDays(bloomDay, m, k)
print(result)  # Output: 3
```

### Additional Resources

[Link to detailed explanation on GeeksforGeeks](https://www.geeksforgeeks.org/minimum-days-to-make-m-bouquets/)

[Link to detailed explanation on Medium](https://poitevinpm.medium.com/leetcode-1482-minimum-number-of-days-to-make-m-bouquets-5e8de3b4a101)

[Link to detailed explanation on AlgoMonster](https://algo.monster/liteproblems/1482)

### Check Out These Videos

[![Video Explanation](https://img.youtube.com/vi/TXAuxeYBTdg/mqdefault.jpg)](https://youtu.be/TXAuxeYBTdg)

[![Video Explanation](https://img.youtube.com/vi/w24SIuukcZI/mqdefault.jpg)](https://youtu.be/w24SIuukcZI)

[![Video Explanation](https://img.youtube.com/vi/oYE6wuYhqZE/mqdefault.jpg)](https://youtu.be/oYE6wuYhqZE)

### Complexity Analysis

- **Time Complexity:** O(n log D), where `n` is the number of flowers and `D` is the range of days to search. The complexity is dominated by the binary search and the check within each search.
- **Space Complexity:** O(1), since no additional space proportional to the input size is required. The calculations are performed in-place.