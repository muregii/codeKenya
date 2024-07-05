# Leetcode - Sort Colors

## Problem Description

Given an array `nums` with `n` objects colored red, white, or blue, sort them **in-place** so that objects of the same color are adjacent, with the colors in the order red, white, and blue. 

We will use the integers `0`, `1`, and `2` to represent the color red, white, and blue, respectively. 

You must solve this problem without using the library's sort function.

**Constraints:**
- `n == nums.length`
- `1 <= n <= 300`
- `nums[i]` is either `0`, `1`, or `2`.

## Solution

To sort the `nums` array in-place with colors red (0), white (1), and blue (2):


1. **Understanding the Problem:**
   - We have an array `nums` with objects colored red, white, or blue, represented by `0`, `1`, and `2` respectively.
   - The task is to sort this array in-place such that all `0`s come first, followed by `1`s, and finally `2`s.
   - The solution should not use built-in sorting functions and must modify `nums` directly.

2. **Dutch National Flag Algorithm:**
   - This problem can be efficiently solved using the Dutch National Flag algorithm by Edsger Dijkstra.
   - The algorithm uses three pointers to sort the array in a single pass:
     - `low` to place the `0`s.
     - `mid` to iterate through the array.
     - `high` to place the `2`s.

3. **Initialize Pointers:**
   - Start with `low` and `mid` at the beginning (`0` index) and `high` at the end (`n-1` index).

4. **Sort the Colors:**
   - Iterate with `mid` pointer:
     - If `nums[mid]` is `0`, swap it with the element at `low`, then increment `low` and `mid`.
     - If `nums[mid]` is `1`, just move `mid` to the next element.
     - If `nums[mid]` is `2`, swap it with the element at `high`, and decrement `high`.

5. **Finish Sorting:**
   - Continue until `mid` surpasses `high`. The array will be sorted with all `0`s at the beginning, followed by `1`s, and `2`s at the end.

### Example

Suppose you have `nums = [2, 0, 2, 1, 1, 0]`.

1. Initialize `low = 0`, `mid = 0`, `high = 5`.
2. `nums[mid]` is `2`. Swap with `nums[high]` and decrement `high`:
   - `nums = [0, 0, 2, 1, 1, 2]`, `low = 0`, `mid = 0`, `high = 4`.
3. `nums[mid]` is `0`. Swap with `nums[low]` and increment `low` and `mid`:
   - `nums = [0, 0, 2, 1, 1, 2]`, `low = 1`, `mid = 1`, `high = 4`.
4. `nums[mid]` is `0`. Swap with `nums[low]` and increment `low` and `mid`:
   - `nums = [0, 0, 2, 1, 1, 2]`, `low = 2`, `mid = 2`, `high = 4`.
5. `nums[mid]` is `2`. Swap with `nums[high]` and decrement `high`:
   - `nums = [0, 0, 1, 1, 2, 2]`, `low = 2`, `mid = 2`, `high = 3`.
6. `nums[mid]` is `1`. Move `mid` to the next element:
   - `nums = [0, 0, 1, 1, 2, 2]`, `low = 2`, `mid = 3`, `high = 3`.
7. `nums[mid]` is `1`. Move `mid` to the next element:
   - `nums = [0, 0, 1, 1, 2, 2]`, `low = 2`, `mid = 4`, `high = 3`.
8. The sorted array is `[0, 0, 1, 1, 2, 2]`.

### Python Code

Here’s how you can implement this solution in Python:

```python
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
       
```

### Usage

To use the solution, create an instance of the `Solution` class and call the `sortColors` method with `nums`:

```python
solution = Solution()
nums = [2, 0, 2, 1, 1, 0]
solution.sortColors(nums)
print(nums)  # Output: [0, 0, 1, 1, 2, 2]
```

### Additional Resources

[Link to detailed explanation on GeeksforGeeks](https://www.geeksforgeeks.org/sort-an-array-of-0s-1s-and-2s/)

[Link to detailed explanation on Medium](https://medium.com/nerd-for-tech/75-sort-colors-15768309bf2f)

[Link to detailed explanation on AlgoMonster](https://algo.monster/liteproblems/75)

### Check Out These Videos

[![Video Explanation](https://img.youtube.com/vi/4xbWSRZHqac/mqdefault.jpg)](https://youtu.be/4xbWSRZHqac)

[![Video Explanation](https://img.youtube.com/vi/6sMssUHgaBs/mqdefault.jpg)](https://youtu.be/6sMssUHgaBs)

[![Video Explanation](https://img.youtube.com/vi/sEQk8xgjx64/mqdefault.jpg)](https://youtu.be/sEQk8xgjx64)

### Complexity Analysis

- **Time Complexity:** O(n), where `n` is the length of `nums`. The algorithm performs a single pass through the array, making it linear in time complexity.
- **Space Complexity:** O(1), since no additional space proportional to the input size is used. The sorting is done in-place.