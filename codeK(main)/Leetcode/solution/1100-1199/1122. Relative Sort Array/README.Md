# Leetcode - Relative Sort Array

## Problem Description

Given two arrays `arr1` and `arr2`, the elements of `arr2` are distinct, and all elements in `arr2` are also in `arr1`.

Sort the elements of `arr1` such that the relative ordering of items in `arr1` are the same as in `arr2`. Elements that do not appear in `arr2` should be placed at the end of `arr1` in **ascending** order.

**Constraints:**
- `1 <= arr1.length, arr2.length <= 1000`
- `0 <= arr1[i], arr2[i] <= 1000`
- All elements of `arr2` are **distinct**.
- Each `arr2[i]` is in `arr1`.

## Solution

To sort `arr1` based on the relative ordering of elements in `arr2`, and place the remaining elements at the end in ascending order:


1. **Understanding the Problem:**
   - You have two arrays: `arr1` and `arr2`. The goal is to sort `arr1` such that the elements appear in the same relative order as they do in `arr2`.
   - Any elements in `arr1` that are not in `arr2` should be placed at the end of `arr1` in ascending order.

2. **Create a Frequency Map:**
   - Use a dictionary to count the occurrences of each element in `arr1`.

3. **Sort According to `arr2`:**
   - Iterate through `arr2`, and for each element, place it in the result array as many times as it appears in `arr1` using the frequency map.

4. **Sort Remaining Elements:**
   - Collect all elements from `arr1` that do not appear in `arr2` and sort them.
   - Append these sorted elements to the result array.

5. **Return the Result:**
   - The final result array will have the elements of `arr1` sorted according to the rules specified.

### Example

Suppose you have `arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]` and `arr2 = [2, 1, 4, 3, 9, 6]`.

1. Create a frequency map for `arr1`:
   - `{2: 3, 3: 2, 1: 1, 4: 1, 6: 1, 7: 1, 9: 1, 19: 1}`

2. Place elements from `arr2` in the result array:
   - `[2, 2, 2, 1, 4, 3, 3, 9, 6]`

3. Sort the remaining elements `[7, 19]`:
   - `[7, 19]`

4. Combine the arrays:
   - `[2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]`

### Python Code

Here’s how you can implement this solution in Python:

```python
class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        
```

### Usage

To use the solution, create an instance of the `Solution` class and call the `relativeSortArray` method with `arr1` and `arr2`:

```python
solution = Solution()
arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
arr2 = [2, 1, 4, 3, 9, 6]
result = solution.relativeSortArray(arr1, arr2)
print(result)  # Output: [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]
```

### Additional Resources

[Link to detailed explanation on GeeksforGeeks](https://www.geeksforgeeks.org/sort-array-according-order-defined-another-array/)

[Link to detailed explanation on Medium](https://donic0211.medium.com/leetcode-1122-relative-sort-array-7035e7afc54a)

[Link to detailed explanation on AlgoMonster](https://algo.monster/liteproblems/1122)

### Check Out These Videos

[![Video Explanation](https://img.youtube.com/vi/OPvcR1e4lfg/mqdefault.jpg)](https://youtu.be/OPvcR1e4lfg)

[![Video Explanation](https://img.youtube.com/vi/4TtA2BfXvuw/mqdefault.jpg)](https://youtu.be/4TtA2BfXvuw)

[![Video Explanation](https://img.youtube.com/vi/1pCkWXT5k2s/mqdefault.jpg)](https://youtu.be/1pCkWXT5k2s)

### Complexity Analysis

- **Time Complexity:** O(n log n + m), where `n` is the length of `arr1` and `m` is the length of `arr2`. Sorting the remaining elements is the dominant term here, which is O(n log n).
- **Space Complexity:** O(n), where `n` is the length of `arr1`. The space is used for the frequency map and the result array.