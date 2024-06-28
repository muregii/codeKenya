# Leetcode - Reverse String

## Problem Description

Write a function that reverses a string. The input string is given as an array of characters `s`.

You must do this by modifying the input array in-place with `O(1)` extra memory.

**Constraints:**
- `1 <= s.length <= 10^5`
- `s[i]` is a printable ASCII character.

## Solution

Reverse the array of characters `s` in-place. This means we should modify the input array directly without using any extra space.

Think of a string as a row of letters. Reverse the order of these letters. So, the letter at the start should move to the end, the letter at the end should move to the start, and we keep doing this until we meet in the middle.

The `reverseString` method takes an array of characters `s` and reverses it in place.

1. **Using Two Pointers:**
   - We can use two pointers: one starting at the beginning of the array (`left`) and the other at the end of the array (`right`).
   - Swap the characters at these two positions.
   - Move the `left` pointer one step to the right and the `right` pointer one step to the left.
   - Repeat this process until the `left` pointer is greater than or equal to the `right` pointer.

2. **Algorithm:**
   - Initialize two pointers, `left` and `right`, at the beginning and end of the array, respectively.
   - While `left` is less than `right`:
     - Swap the characters at `left` and `right`.
     - Move `left` one step to the right.
     - Move `right` one step to the left.
   - The array is now reversed in place.


Start with two pointers, one at the beginning and one at the end of the string. We swap the letters these pointers are pointing to. Then we move the pointers towards the center and keep swapping until they meet in the middle.


```python
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
```

## Usage

To use the solution, create an instance of the `Solution` class and call the `reverseString` method with the array of characters `s`:

```python
solution = Solution()
s = ['h', 'e', 'l', 'l', 'o']
solution.reverseString(s)
print(s)  # Output: ['o', 'l', 'l', 'e', 'h']
```


[Link to detailed explanation on Medium](https://medium.com/@justcode/leetcode-344-reverse-string-a4de5957d622)




## Check Out this video

[![Video Explanation](https://img.youtube.com/vi/_d0T_2Lk2qA/mqdefault.jpg)](https://youtu.be/_d0T_2Lk2qA)


[![Video Explanation](https://img.youtube.com/vi/5keS487q67M/mqdefault.jpg)](https://youtu.be/5keS487q67M)


[![Video Explanation](https://img.youtube.com/vi/LMeYeTXrGak/mqdefault.jpg)](https://youtu.be/LMeYeTXrGak)



## Complexity Analysis

- **Time Complexity:** O(n), where n is the length of the array `s`. We iterate through half of the array, performing swaps.
- **Space Complexity:** O(1), as we are using a constant amount of extra space for the two pointers.