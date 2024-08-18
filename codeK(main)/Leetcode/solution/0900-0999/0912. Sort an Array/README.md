# Leetcode - Sort an Array

## Problem Description

Given an array of integers `nums`, sort the array in **ascending** order and return it.

You must solve the problem **without using any built-in** functions in `O(nlog(n))` time complexity and with the smallest space complexity possible.

**Constraints:**
- `1 <= nums.length <= 5 * 10^4`
- `-5 * 10^4 <= nums[i] <= 5 * 10^4`

## Solution

**Understanding the Problem:**
   - We need to sort an array of integers in ascending order without using any built-in sorting functions.
   - The solution must work efficiently, within O(n log n) time complexity, and with minimal space usage.

**Breaking It Down**
   - **Sorting Requirement.**
     The task is to arrange the numbers from the smallest to the largest.
     Since built-in functions are not allowed, we need to implement a sorting algorithm manually.
     
   - **Choosing a Sorting Algorithm.**
     To meet the O(n log n) time complexity, we can consider algorithms like Merge Sort, Quick Sort, or Heap Sort.
     - **Merge Sort:** Divides the array into halves, sorts each half, and then merges them. It has a time complexity of O(n log n) and requires additional space for merging.
     - **Quick Sort:** Uses a pivot to partition the array into smaller subarrays, sorts them recursively, and has a time complexity of O(n log n) on average.
     - **Heap Sort:** Builds a heap from the array and repeatedly extracts the minimum (or maximum) element to sort the array. It also has O(n log n) time complexity and operates in place, making it space efficient.
     
   - **Implementation Approach.**
     We can choose Heap Sort for this problem because it operates in place, minimizing space usage while meeting the time complexity requirement.

**Algorithm Steps:**
   - **Heap Construction:** Convert the array into a heap where the smallest element can be efficiently extracted.
   - **Heap Sort:** Repeatedly extract the smallest element from the heap and place it in its correct position in the array.
   - **Return the Sorted Array:** The array is now sorted in ascending order.

### Python Code

```python
class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
       
```

### Example

```python
# Input
nums = [5, 2, 3, 1]

# Output
[1, 2, 3, 5]
```

### Explanation
1. **Heapify Step:** The array is converted into a heap.
2. **Sorting Step:** Elements are extracted from the heap and placed into their correct position, resulting in a sorted array.
3. **Result:** The array is sorted in ascending order.

### Usage

To use the solution, create an instance of the `Solution` class and call the `sortArray` method with the `nums` array:

```python
# Example usage
solution = Solution()
nums = [5, 2, 3, 1]
sorted_nums = solution.sortArray(nums)
print(sorted_nums)  # Output: [1, 2, 3, 5]
```

### Additional Resources

[Link to detailed explanation on Algo Monster](https://algo.monster/liteproblems/912)

[Link to detailed explanation on Medium](https://nileshsaini09.medium.com/sort-an-array-2e1138019e0d)


### Check Out These Video(s)

[![Video Explanation](https://img.youtube.com/vi/FiawvsBgYVs/mqdefault.jpg)](https://youtu.be/FiawvsBgYVs)

[![Video Explanation](https://img.youtube.com/vi/MsYZSinhuFo/mqdefault.jpg)](https://youtu.be/MsYZSinhuFo)

### Complexity Analysis

- **Time Complexity:** O(n log n), where `n` is the length of the `nums` array. The heap sort algorithm ensures this time complexity.
- **Space Complexity:** O(1), since Heap Sort is an in-place sorting algorithm that requires only a constant amount of extra space.