# Leetcode - Minimum Swaps to Group All 1's Together II

## Problem Description

A **swap** is defined as taking two **distinct** positions in an array and swapping the values in them.

A **circular** array is defined as an array where the **first** element and the **last** element are considered **adjacent**.

Given a **binary circular** array `nums`, return *the minimum number of swaps required to group all 1's present in the array together at **any location***.

**Constraints:**
- `1 <= nums.length <= 10^5`
- `nums[i]` is either `0` or `1`.

## Solution

**Understanding the Problem:**
   - We are given a binary array where the first and last elements are considered adjacent (circular array).
   - The goal is to calculate the minimum number of swaps needed to group all `1`s together in any contiguous block in the array.

**Breaking It Down**
   - **Counting Total 1's:**
     - First, we need to determine how many `1`s are present in the array since this will dictate the size of the block we need to form.
     
   - **Sliding Window Technique:**
     - Given that the array is circular, we use a sliding window of size equal to the total number of `1`s.
     - We calculate how many `0`s exist in this window (which indicates how many swaps are needed to group the `1`s together).
     - By sliding this window across the array, we can determine the minimum number of swaps required.
     
   - **Circular Handling:**
     - Since the array is circular, we consider the end of the array wrapping around to the start to handle the sliding window correctly.

**Implementation Approach:**
   - Count the total number of `1`s in the array.
   - Create a sliding window of the same length as the count of `1`s and calculate the number of `0`s in this window.
   - Slide the window across the array and keep track of the minimum number of `0`s encountered (indicating the minimum swaps required).
   - Return this minimum value.

**Algorithm Steps:**
   - **Count Total 1's:** Calculate the number of `1`s in the array.
   - **Initialize Sliding Window:** Set up a sliding window of size equal to the number of `1`s and count the number of `0`s in the first window.
   - **Slide the Window:** Move the window across the array, updating the count of `0`s by subtracting the outgoing element and adding the incoming element.
   - **Find Minimum Swaps:** Track the minimum number of `0`s encountered during the sliding, which corresponds to the minimum number of swaps needed.

### Python Code

```python
class Solution(object):
    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Example

```python
# Input
nums = [1, 0, 1, 0, 1, 1]

# Output
1
```

### Explanation
1. **Count 1's:** The total number of `1`s in the array is 4.
2. **Sliding Window:** Using a window size of 4, we slide through the array to count the minimum number of `0`s in each window.
3. **Result:** The minimum number of `0`s encountered in any window is 1, so the minimum number of swaps needed is 1.

### Usage

To use the solution, create an instance of the `Solution` class and call the `minSwaps` method with the `nums` array:

```python
# Example usage
solution = Solution()
nums = [1, 0, 1, 0, 1, 1]
result = solution.minSwaps(nums)
print(result)  # Output: 1
```

### Additional Resources

[Link to detailed explanation on Algo Monster](https://algo.monster/liteproblems/2134)

[Link to detailed explanation on Geeksforgeeks](https://www.geeksforgeeks.org/minimum-swaps-required-group-1s-together/)

### Check Out These Video(s)

[![Video Explanation](https://img.youtube.com/vi/FjEi39DHTkI/mqdefault.jpg)](https://youtu.be/FjEi39DHTkI)

[![Video Explanation](https://img.youtube.com/vi/BueoreUIkcE/mqdefault.jpg)](https://youtu.be/BueoreUIkcE)

### Complexity Analysis

- **Time Complexity:** O(n), where `n` is the length of the `nums` array. We iterate through the array once to count the `1`s and then slide the window across the array.
- **Space Complexity:** O(n), for the extended array to handle the circular nature of the array.