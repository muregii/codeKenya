# Leetcode - Wonderful Substrings

## Problem Description

A **wonderful string** is a string where **at most one** letter appears an **odd** number of times.

For example, `"ccjjc"` and `"abab"` are wonderful, but `"ab"` is not.

Given a string `word` that consists of the first ten lowercase English letters (`'a'` through `'j'`), return the *number of wonderful non-empty substrings in `word`*. *If the same substring appears multiple times in `word`, then count each occurrence separately.*

A **substring** is a contiguous sequence of characters in a string.

## Solution

To solve this problem, we can use a prefix sum approach combined with bit manipulation.

Here's how we can approach this problem:

1. Initialize a dictionary `count` to store the count of occurrences of each prefix XOR value.
2. Initialize variables `result` and `prefix` to 0.
3. Iterate through each character `c` in the string `word`.
4. Update the `prefix` variable by XORing the current prefix with the bit representation of `c`.
5. Increment the count of the current `prefix` in the `count` dictionary.
6. For each bit `i` in the binary representation of `prefix`, calculate the count of wonderful substrings where the `i`-th letter is flipped.
7. Update the result by adding the count of wonderful substrings for the current prefix.
8. Increment the count of the current prefix in the `count` dictionary.
9. Return the result.

By using prefix XOR values and bit manipulation, we can efficiently count the number of wonderful substrings in the given string.

## Usage

To use the solution, create an instance of the `Solution` class and call the `wonderfulSubstrings` method with the input parameter `word`:

```python
solution = Solution()
# Define the input string word
# word = "ccjjc"
# Call the wonderfulSubstrings method
result = solution.wonderfulSubstrings(word)
print(result)
```

```python
# word = "ccjjc"
```

[Link to detailed explanation on Geeksforgeeks](https://www.geeksforgeeks.org/longest-common-substring-dp-29/)


[Link to detailed explanation on Medium](https://algomonster.medium.com/leetcode-1915-number-of-wonderful-substrings-fd94fc49de77)


[Link to detailed explanation on Medium](https://medium.com/leetcode-patterns/leetcode-pattern-2-sliding-windows-for-strings-e19af105316b)


[Link to detailed explanation on Medium](https://medium.com/kode-shaft/solve-minimum-window-substring-problem-9cb3544eeb91)

## Check Out this video

[![Video Explanation](https://img.youtube.com/vi/P6i1qj8DMZk/mqdefault.jpg)](https://youtu.be/P6i1qj8DMZk)


[![Video Explanation](https://img.youtube.com/vi/EnBTWY52n_A/mqdefault.jpg)](https://youtu.be/EnBTWY52n_A)


[![Video Explanation](https://img.youtube.com/vi/mjQvGZO-3fs/mqdefault.jpg)](https://youtu.be/mjQvGZO-3fs)


## Complexity Analysis

- **Time Complexity:** O(n), where n is the length of the input string `word`. We iterate through each character once.
- **Space Complexity:** O(1). We use only constant extra space for storing intermediate results.