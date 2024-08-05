# Leetcode - Reverse Substrings Between Each Pair of Parentheses

## Problem Description

You are given a string `s` that consists of lower case English letters and brackets.

Reverse the strings in each pair of matching parentheses, starting from the innermost one.

Your result should not contain any brackets.

**Constraints:**
- `1 <= s.length <= 2000`
- `s` only contains lower case English characters and parentheses.
- It is guaranteed that all parentheses are balanced.

## Solution

To solve this problem, reverse the substrings within each pair of matching parentheses, starting from the innermost ones. This involves using a stack to manage the parentheses and their contents.

1. **Understanding the Problem:**
   - Each pair of parentheses indicates a portion of the string that needs to be reversed.
   - The reversal starts from the innermost pair and works outwards.
   - Once reversed, the parentheses are removed from the result.

2. **Simulating the Process:**
   - Use a stack to keep track of characters and handle nested parentheses.
   - Push characters onto the stack until a closing parenthesis `)` is encountered.
   - Upon encountering `)`, pop characters from the stack until an opening parenthesis `(` is found, reverse the popped characters, and push them back onto the stack.

3. **Algorithm Steps:**
   - Initialize an empty stack.
   - Iterate through each character in the string `s`:
     - If the character is `)`, pop characters from the stack until `(` is found, reverse the popped characters, and push them back onto the stack.
     - Otherwise, push the character onto the stack.
   - Join the characters in the stack to form the final result string without any parentheses.

### Example

Suppose you have `s = "(u(love)i)"`:

1. Initial string: `(u(love)i)`
2. Process the innermost parentheses first:
   - `(u(love)i)` -> `love` is reversed to `evol`.
   - Stack: `['(', 'u', '(', 'e', 'v', 'o', 'l', ')', 'i']`
   - After reversing `love`: `['(', 'u', 'e', 'v', 'o', 'l', 'i']`
3. Process the next outer parentheses:
   - `u(evoli)` -> `u` and `i` remain, `evoli` is reversed to `ilove`.
   - Stack: `['u', 'i', 'l', 'o', 'v', 'e']`
4. Final result: `iloveu`.

### Python Code

```python
class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        
```

### Usage

To use the solution, create an instance of the `Solution` class and call the `reverseParentheses` method with the string `s`:

```python
# Example usage
solution = Solution()
s = "(u(love)i)"
result = solution.reverseParentheses(s)
print(result)  # Output: "iloveu"
```

### Additional Resources

[Link to detailed explanation on GeeksforGeeks](https://www.geeksforgeeks.org/reverse-substrings-between-each-pair-of-parenthesis/)

[Link to detailed explanation on Algo Monster](https://algo.monster/liteproblems/1190)

### Check Out These Videos

[![Video Explanation](https://img.youtube.com/vi/n_pCJmg-RyU/mqdefault.jpg)](https://youtu.be/n_pCJmg-RyU)

[![Video Explanation](https://img.youtube.com/vi/N5hBo4dgg8g/mqdefault.jpg)](https://youtu.be/N5hBo4dgg8g)

[![Video Explanation](https://img.youtube.com/vi/65wVufni3tg/mqdefault.jpg)](https://youtu.be/65wVufni3tg)

### Complexity Analysis

- **Time Complexity:** O(n), as each character in the string is processed once.
- **Space Complexity:** O(n), due to the use of a stack to store characters and handle nested parentheses.