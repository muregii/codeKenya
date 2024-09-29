# Leetcode - Convert 1D Array Into 2D Array

## Problem Description

You are given a **0-indexed** 1-dimensional (1D) integer array `original`, and two integers `m` and `n`. Your task is to create a 2-dimensional (2D) array with `m` rows and `n` columns using all the elements from `original`.

The elements from indices `0` to `n-1` (**inclusive**) of `original` should form the first row of the constructed 2D array. The elements from indices `n` to `2 * n - 1` (**inclusive**) should form the second row, and so on.

Return _an `m x n` 2D array constructed according to the above procedure, or an empty 2D array if it is impossible._

### Constraints:

- `1 <= original.length <= 5 * 10^4`
- `1 <= original[i] <= 10^5`
- `1 <= m, n <= 4 * 10^4`

## Solution

### Understanding the Problem:

We are tasked with converting a 1D array into a 2D array. To achieve this, the product of the number of rows (`m`) and columns (`n`) should be equal to the length of the `original` array. If the total number of elements in the `original` array matches the required elements for the 2D array (`m * n`), we can convert the array. Otherwise, we return an empty array.

### Breaking It Down:

1. **Check Validity:**
   - First, check if the number of elements in `original` matches `m * n`. If not, return an empty array.
2. **Construct 2D Array:**
   - Use a loop to slice the `original` array into `n` elements for each row and append them to the 2D array.

### Algorithm Steps:

1. **Check Length:**
   - If `len(original) != m * n`, return an empty array.
2. **Construct the 2D Array:**

   - Iterate over the `original` array, taking `n` elements at a time, and append them as rows to the 2D array.

3. **Return the Result:**
   - Return the constructed 2D array.

### Python Code

```python
class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """

```

### Example

```python
# Input:
original = [1, 2, 3, 4]
m = 2
n = 2

# Output:
[[1, 2], [3, 4]]
```

### Explanation:

1. The array `original = [1, 2, 3, 4]` has 4 elements.
2. We are tasked with creating a 2D array of dimensions `2 x 2`.
3. Since `2 * 2 = 4` equals the length of `original`, we can convert it into:
   - The first row: `[1, 2]`
   - The second row: `[3, 4]`
4. The resulting 2D array is `[[1, 2], [3, 4]]`.

### Usage

To use this solution, create an instance of the `Solution` class and call the `construct2DArray` method with the input parameters:

```python
solution = Solution()
original = [1, 2, 3, 4]
m = 2
n = 2
result = solution.construct2DArray(original, m, n)
print(result)  # Output: [[1, 2], [3, 4]]
```

### Additional Resources

- [Algo Monster Article](https://algo.monster/liteproblems/2022)

- [GeeksforGeeks Article ](https://www.geeksforgeeks.org/python-flatten-a-2d-numpy-array-into-1d-array/)

- [GeeksforGeeks Article ](https://www.geeksforgeeks.org/convert-a-1d-array-to-a-2d-numpy-array/)

### Check Out These Video(s):

[![Video Explanation](https://img.youtube.com/vi/AvLVZ3oLOGw/mqdefault.jpg)](https://youtu.be/AvLVZ3oLOGw)

[![Video Explanation](https://img.youtube.com/vi/l-VLzZ2riTc/mqdefault.jpg)](https://youtu.be/l-VLzZ2riTc)

### Complexity Analysis

- **Time Complexity:** O(m \* n), where `m` is the number of rows and `n` is the number of columns. We need to iterate over each element of the `original` array once to construct the 2D array.
- **Space Complexity:** O(m \* n), as we need to store the result in a 2D array with `m` rows and `n` columns.
