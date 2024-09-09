# Leetcode - Maximum Distance in Arrays

## Problem Description

You are given `m` `arrays`, where each array is sorted in **ascending order**.

You can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers `a` and `b` to be their absolute difference `|a - b|`.

Return *the maximum distance*.

**Constraints:**
- `m == arrays.length`
- `2 <= m <= 10^5`
- `1 <= arrays[i].length <= 500`
- `-10^4 <= arrays[i][j] <= 10^4`
- `arrays[i]` is sorted in ascending order.
- There will be at most `10^5` integers in all the arrays.

## Solution

**Understanding the Problem:**
   - We need to find the maximum distance between pairs of elements from different arrays.
   - Each array is sorted in ascending order, so for each array, the smallest element is the first element, and the largest element is the last.
   - To maximize the distance, we need to calculate the absolute difference between the largest element of one array and the smallest element of another array.

**Breaking It Down**
   - **Key Observations:**
     - Since each array is sorted, the smallest element of any array will always be the first element (`arrays[i][0]`).
     - The largest element of any array will always be the last element (`arrays[i][-1]`).
   - **Maximizing the Distance:**
     - To find the maximum distance, we can compare the largest element of one array with the smallest element of another array.
     - The goal is to maximize the absolute difference between these values as we iterate through the arrays.

**Implementation Approach:**
   - Track the **minimum** element (`min_value`) encountered so far (from the first elements of arrays).
   - Track the **maximum** element (`max_value`) encountered so far (from the last elements of arrays).
   - Iterate through all arrays:
     - For each array, calculate the distance between its largest element and the global `min_value`.
     - Also, calculate the distance between its smallest element and the global `max_value`.
     - Update the result with the maximum of these distances.
   - Continue updating `min_value` and `max_value` as you traverse the arrays.

**Algorithm Steps:**
   1. Initialize `min_value` to the first element of the first array.
   2. Initialize `max_value` to the last element of the first array.
   3. For each array (starting from the second one):
      - Calculate the distance between the current array's largest element and the global `min_value`.
      - Calculate the distance between the current array's smallest element and the global `max_value`.
      - Update the maximum distance found so far.
      - Update `min_value` and `max_value` as necessary.
   4. Return the maximum distance.

### Python Code

```python
class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        
```

### Example

```python
# Input
arrays = [[1, 2, 3], [4, 5], [1, 2, 3]]

# Output
4
```

### Explanation

- First array's largest element is `3`, and the second array's smallest element is `4`, yielding a distance of `|3 - 1| = 2`.
- For the third array, the largest element is `3`, and the smallest is `1`, but this doesn’t yield a larger distance.
- The maximum distance found is `4`, which is from comparing the largest element `5` from the second array and the smallest element `1` from the first array.

### Usage

To use the solution, create an instance of the `Solution` class and call the `maxDistance` method with the `arrays` list:

```python
# Example usage
solution = Solution()
arrays = [[1, 2, 3], [4, 5], [1, 2, 3]]
result = solution.maxDistance(arrays)
print(result)  # Output: 4
```

### Additional Resources

[Link to detailed explanation on Algo Monster](https://algo.monster/liteproblems/624)

[Link to detailed explanation on Medium](https://medium.com/solvingalgo/solving-algorithmic-problems-max-distance-in-an-array-7e8c9f71c8b)

[Link to detailed explanation on Geeksforgeeks](https://www.geeksforgeeks.org/maximum-distance-between-two-unequal-elements/)

### Check Out These Video(s)

[![Video Explanation](https://img.youtube.com/vi/J0yYlj_oVTI/mqdefault.jpg)](https://youtu.be/J0yYlj_oVTI)


### Complexity Analysis

- **Time Complexity:** O(m), where `m` is the number of arrays. We process each array exactly once.
- **Space Complexity:** O(1), as we are only using a few variables beyond the input data to keep track of `min_value`, `max_value`, and the result.