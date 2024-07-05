# Leetcode - Height Checker

## Problem Description

A school is trying to take an annual photo of all the students. The students are asked to stand in a single file line in **non-decreasing order** by height. Let this ordering be represented by the integer array `expected` where `expected[i]` is the expected height of the `ith` student in line.

You are given an integer array `heights` representing the **current order** that the students are standing in. Each `heights[i]` is the height of the ith student in line (**0-indexed**).

*Return the **number of indices** where `heights[i]` is not equal to `expected[i]`.*

**Constraints:**
- `1 <= heights.length <= 100`
- `1 <= heights[i] <= 100`

## Solution

To find the number of students who are not standing in the expected order by height:


1. **Understanding the Problem:**
   - We have an array `heights` which tells us the current height of students in a line.
   - We need to compare this with an `expected` array which represents the sorted order of the students by height.
   - Our task is to count how many students are not standing in their correct position.

2. **Generate the Expected Array:**
   - The `expected` array is just the sorted version of the `heights` array. By sorting the `heights` array, we get the `expected` order.

3. **Compare Heights with Expected Order:**
   - We then compare each element in the `heights` array with the corresponding element in the `expected` array.
   - For each index where the heights do not match, we increment our count.

4. **Return the Count:**
   - The final count gives us the number of students who are not standing in their correct positions according to the expected height order.

### Example

Imagine you have a list of students' heights `[1, 1, 4, 2, 1, 3]`. The expected order is `[1, 1, 1, 2, 3, 4]`.

1. Compare each student’s height with the expected order:
   - Index 0: 1 vs. 1 (Correct)
   - Index 1: 1 vs. 1 (Correct)
   - Index 2: 4 vs. 1 (Incorrect)
   - Index 3: 2 vs. 2 (Correct)
   - Index 4: 1 vs. 3 (Incorrect)
   - Index 5: 3 vs. 4 (Incorrect)

2. We see that 3 students are not standing in the correct positions.

### Python Code


```python
class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

```

### Usage

To use the solution, create an instance of the `Solution` class and call the `heightChecker` method with the array of heights:

```python
solution = Solution()
heights = [1, 1, 4, 2, 1, 3]
result = solution.heightChecker(heights)
print(result)  # Output: 3, because there are 3 students who are not in the correct positions.
```

### Additional Resources

[Link to detailed explanation on Medium](https://medium.com/@haroon.siddiqui025/leetcode-q1051-height-checker-easy-e2bf8b3033d3)

[Link to detailed explanation on AlgoMonster](https://algo.monster/liteproblems/1051)

### Check Out These Videos

[![Video Explanation](https://img.youtube.com/vi/mQAoeYaE3Xk/mqdefault.jpg)](https://youtu.be/mQAoeYaE3Xk)

[![Video Explanation](https://img.youtube.com/vi/7s7G42nWS1E/mqdefault.jpg)](https://youtu.be/7s7G42nWS1E)


### Complexity Analysis

- **Time Complexity:** O(n log n), where `n` is the number of elements in `heights`. The dominant term here is due to the sorting operation, which is O(n log n).
- **Space Complexity:** O(n), where `n` is the number of elements in `heights`. This is due to the space required to store the `expected` array.