# Leetcode - Maximum Score From Removing Substrings

## Problem Description

You are given a string `s` and two integers `x` and `y`. You can perform two types of operations any number of times:
- Remove substring `"ab"` and gain `x` points. 
  - For example, removing `"ab"` from `"cabxbae"` results in `"cxbae"`.
- Remove substring `"ba"` and gain `y` points. 
  - For example, removing `"ba"` from `"cabxbae"` results in `"cabxe"`.

Return *the maximum points you can gain after applying the above operations on `s`*.

**Constraints:**
- `1 <= s.length <= 10^5`
- `1 <= x, y <= 10^4`
- `s` consists of lowercase English letters.

## Solution

To solve this problem, maximize the points gained by strategically removing the substrings `"ab"` and `"ba"`. Depending on the values of `x` and `y`, prioritize removing one substring over the other to gain maximum points.

1. **Understanding the Problem:**
   - We have two types of substrings to remove: `"ab"` and `"ba"`.
   - Each removal yields points (`x` for `"ab"`, `y` for `"ba"`).
   - We need to decide the order of removal based on which operation yields more points.

2. **Simulating the Process:**
   - If `x >= y`, prioritize removing `"ab"` first, then remove any remaining `"ba"`.
   - If `y > x`, prioritize removing `"ba"` first, then remove any remaining `"ab"`.
   - Use a stack to efficiently manage the removal process.

3. **Algorithm Steps:**
   - Initialize a stack to process the string.
   - Iterate through each character in the string `s` and use the stack to remove substrings according to the prioritized order.
   - Calculate and return the total points gained.

### Example

Suppose you have `s = "abcbab"`, `x = 3`, and `y = 4`:

1. Initial string: `abcbab`
2. Since `y > x`, prioritize removing `"ba"`:
   - After removing `"ba"`: `abcba` -> `acca`
   - Remaining string after removing `"ba"`: `acca`
3. Now remove any remaining `"ab"`:
   - No `"ab"` left in `acca`.
4. Total points: 4 (for one `"ba"` removal).

### Python Code

```python
class Solution(object):
    def maximumGain(self, s, x, y):
        """
        :type s: str
        :type x: int
        :type y: int
        :rtype: int
        """
        
```

### Usage

To use the solution, create an instance of the `Solution` class and call the `maximumGain` method with the string `s` and integers `x` and `y`:

```python
# Example usage
solution = Solution()
s = "abcbab"
x = 3
y = 4
result = solution.maximumGain(s, x, y)
print(result)  # Output: 7
```

### Additional Resources

[Link to detailed explanation on GeeksforGeeks](https://www.geeksforgeeks.org/maximum-score-by-removing-substrings-made-up-of-single-distinct-character/)

[Link to detailed explanation on Medium](https://jimmy-shen.medium.com/stack-1717-maximum-score-from-removing-substrings-b8c2464b0495)

[Link to detailed explanation on Algo Monster](https://algo.monster/liteproblems/1717)

### Check Out These Videos

[![Video Explanation](https://img.youtube.com/vi/r_3a0oG1VcY/mqdefault.jpg)](https://youtu.be/r_3a0oG1VcY)

[![Video Explanation](https://img.youtube.com/vi/WTo5dh6pIis/mqdefault.jpg)](https://youtu.be/WTo5dh6pIis)

[![Video Explanation](https://img.youtube.com/vi/jxng2IcJyCk/mqdefault.jpg)](https://youtu.be/jxng2IcJyCk)

### Complexity Analysis

- **Time Complexity:** O(n), as each character in the string is processed once.
- **Space Complexity:** O(n), due to the use of a stack to store characters and handle substrings.