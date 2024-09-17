# Leetcode - Number Complement

## Problem Description

The **complement** of an integer is the integer you get when you flip all the `0`'s to `1`'s and all the `1`'s to `0`'s in its binary representation.

- For example, The integer `5` is `"101"` in binary and its complement is `"010"` which is the integer 2.


Given an integer `num`, return *its complement*.

### Constraints:
- `1 <= num < 2^31`

## Solution

**Understanding the Problem:**
- The task is to compute the complement of an integer `num` by flipping all the bits of its binary representation. This means converting each `1` to `0` and each `0` to `1`.
  
- For example, the integer `5` has the binary representation `"101"`. Flipping the bits gives `"010"`, which is equal to `2` in decimal.

**Breaking It Down:**
- To get the complement, we need to identify the bit length of the number `num` and construct a mask that has all bits set to `1` (of the same length as `num`). Then, we perform a bitwise XOR between the mask and `num` to flip its bits.
  
**Key Concepts:**
- **Bit Manipulation**: The complement of a number can be computed by XORing it with a mask of all 1’s of the same bit length.
  
  For example:
  - `5` (binary: `101`) with a mask of `111` (which is `7` in decimal) will yield `010` (which is `2` in decimal).
  
**Steps to Solve:**
1. **Find the bit length of the number**: Determine how many bits are required to represent `num`.
2. **Create a mask**: Construct a number with all bits set to `1` for the length of `num`'s bit representation.
3. **Compute the complement**: XOR the number with the mask to flip its bits.

**Implementation Approach:**
- We use bitwise operations to generate the complement of the number:
  - First, calculate the bit length of `num`.
  - Then, construct a mask with all bits set to `1` for that bit length.
  - Finally, XOR `num` with this mask to get the complement.

### Python Code

```python
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        
```

### Example

```python
# Input
num = 5

# Output
2
```

### Explanation:
1. The binary representation of `5` is `"101"`.
2. The complement of `"101"` is `"010"`, which equals `2` in decimal.

### Usage

To use the solution, create an instance of the `Solution` class and call the `findComplement` method with the input integer `num`:

```python
# Example usage
solution = Solution()
num = 5
result = solution.findComplement(num)
print(result)  # Output: 2
```

### Additional Resources

[Link to detailed explanation on Algo Monster](https://algo.monster/liteproblems/476)

[Link to detailed explanation on Medium](https://medium.com/@Harshit_Raj_14/476-number-complement-easy-leetcode-problem-full-solution-and-approach-explained-e321ac3773c0)

### Check Out These Video(s)

[![Video Explanation](https://img.youtube.com/vi/LA1BnKiarEQ/mqdefault.jpg)](https://youtu.be/LA1BnKiarEQ)

### Complexity Analysis

- **Time Complexity:** O(1), because bitwise operations and determining the bit length take constant time.
- **Space Complexity:** O(1), since we are using a constant amount of space for the mask and the result.