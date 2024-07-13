# Leetcode - Magnetic Force Between Two Balls

## Problem Description

In the universe Earth C-137, Rick discovered a special form of magnetic force between two balls if they are put in his new invented basket. Rick has `n` empty baskets, the `ith` basket is at `position[i]`, Morty has `m` balls and needs to distribute the balls into the baskets such that the **minimum magnetic force** between any two balls is **maximum**.

Rick stated that magnetic force between two different balls at positions `x` and `y` is `|x - y|`.

Given the integer array `position` and the integer `m`. Return *the required force*.

**Constraints:**
- `n == position.length`
- `2 <= n <= 10^5`
- `1 <= position[i] <= 10^9`
- All integers in `position` are **distinct**.
- `2 <= m <= position.length`

## Solution

To determine the maximum minimum magnetic force between any two balls, use a binary search approach on the possible forces.

1. **Understanding the Problem:**
   - Place `m` balls into `n` baskets such that the minimum magnetic force between any two balls is maximized.
   - The magnetic force between two balls at positions `x` and `y` is `|x - y|`.
   - We need to find the maximum value of this minimum force.

2. **Using a Binary Search Approach:**
   - Use binary search to find the maximum minimum magnetic force.
   - For each mid value in the binary search, check if it’s possible to place the balls with at least that minimum force.

3. **Algorithm Steps:**
   - Sort the `position` array.
   - Initialize `left` to 1 (minimum possible force) and `right` to `position[-1] - position[0]` (maximum possible force).
   - Perform binary search:
     - Calculate `mid`.
     - Check if it’s possible to place `m` balls with at least `mid` distance apart using a helper function.
     - Adjust `left` and `right` based on the result of the helper function.
   - The result will be the maximum value of the minimum force that allows placing `m` balls.

### Example

Suppose you have `position = [1, 2, 3, 4, 7]` and `m = 3`.

1. Sort `position`: `[1, 2, 3, 4, 7]`
2. Initialize `left = 1` and `right = 6`.
3. Perform binary search:
   - Check if it’s possible to place `3` balls with at least `3` distance apart:
     - Possible placements: `[1, 4, 7]`.
   - Adjust `left` to `3`.
4. Check if it’s possible to place `3` balls with at least `4` distance apart:
   - Possible placements: `[1, 7]`.
   - Not possible, adjust `right` to `3`.

The maximum minimum magnetic force is `3`.

### Python Code


```python
class Solution(object):
    def maxDistance(self, position, m):
        """
        :type position: List[int]
        :type m: int
        :rtype: int
        """
        
```

### Usage

To use the solution, create an instance of the `Solution` class and call the `maxDistance` method with `position` and `m`:

```python
solution = Solution()
position = [1, 2, 3, 4, 7]
m = 3
result = solution.maxDistance(position, m)
print(result)  # Output: 3
```

### Additional Resources

[Link to detailed explanation on Medium](https://medium.com/@EverusLainus/magnetic-force-between-two-balls-b6bf5752f201)

[Link to detailed explanation on AlgoMonster](https://algo.monster/liteproblems/1552)

### Check Out These Videos

[![Video Explanation](https://img.youtube.com/vi/MXnZPSPqkBM/mqdefault.jpg)](https://youtu.be/MXnZPSPqkBM)


### Complexity Analysis

- **Time Complexity:** O(n log D), where `n` is the number of baskets and `D` is the range of possible distances. The complexity is dominated by the binary search and the check within each search.
- **Space Complexity:** O(1), since no additional space proportional to the input size is required. The calculations are performed in-place.