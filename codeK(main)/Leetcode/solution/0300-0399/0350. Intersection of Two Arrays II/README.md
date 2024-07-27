# Leetcode - Intersection of Two Arrays II

## Problem Description

Given two integer arrays `nums1` and `nums2`, return *an array of their intersection*. Each element in the result must appear as many times as it shows in both arrays, and you may return the result in **any order**.

**Constraints:**
- `1 <= nums1.length, nums2.length <= 1000`
- `0 <= nums1[i], nums2[i] <= 1000`

## Solution

To find the intersection of two arrays where each element appears as many times as it does in both arrays, use a dictionary to count the occurrences of elements in one array and then iterate through the other array to find common elements.

1. **Understanding the Problem:**
   - Find common elements between two arrays.
   - Each element in the result must appear as many times as it does in both arrays.

2. **Using a Dictionary for Counting:**
   - Use a dictionary to count the occurrences of each element in `nums1`.
   - Iterate through `nums2` and check if the element is present in the dictionary and its count is greater than 0.
   - If it is, add the element to the result and decrement its count in the dictionary.

3. **Algorithm Steps:**
   - Create a dictionary to store the counts of elements in `nums1`.
   - Iterate through `nums1` and populate the dictionary with the counts of each element.
   - Initialize an empty list to store the result.
   - Iterate through `nums2` and check if the current element is in the dictionary and its count is greater than 0.
   - If it is, append the element to the result list and decrement its count in the dictionary.
   - Return the result list.

### Example

Suppose you have the following arrays:

```
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
```

- Create a dictionary to count elements in `nums1`:
  - {1: 2, 2: 2}

- Iterate through `nums2` and find common elements:
  - 2 is in the dictionary with count 2, add to result and decrement count: {1: 2, 2: 1}, result = [2]
  - 2 is in the dictionary with count 1, add to result and decrement count: {1: 2, 2: 0}, result = [2, 2]

- Return the result: [2, 2]

### Python Code

```python
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
```

### Usage

To use the solution, create an instance of the `Solution` class and call the `intersect` method with the two arrays:

```python
solution = Solution()
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
result = solution.intersect(nums1, nums2)
print(result)  # Output: [2, 2]
```

### Additional Resources

[Link to detailed explanation on Algo Monster](https://algo.monster/liteproblems/350)

[Link to detailed explanation on Medium](https://medium.com/@punitkmr/intersection-of-two-arrays-ii-ffb26f04dfd1)

### Check Out These Videos

[![Video Explanation](https://img.youtube.com/vi/T6bVlhwscuM/mqdefault.jpg)](https://youtu.be/T6bVlhwscuM)

[![Video Explanation](https://img.youtube.com/vi/ctOkl71esQg/mqdefault.jpg)](https://youtu.be/ctOkl71esQg)

[![Video Explanation](https://img.youtube.com/vi/fwUTXaMom6U/mqdefault.jpg)](https://youtu.be/fwUTXaMom6U)


### Complexity Analysis

- **Time Complexity:** O(n + m), where `n` is the length of `nums1` and `m` is the length of `nums2`. We traverse both arrays once.
- **Space Complexity:** O(min(n, m)), for storing the counts of elements in the smaller array.