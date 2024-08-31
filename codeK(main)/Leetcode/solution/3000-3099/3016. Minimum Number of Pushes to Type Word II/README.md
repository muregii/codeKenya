# Leetcode - Minimum Number of Pushes to Type Word II

## Problem Description

You are given a string `word` containing lowercase English letters.

Telephone keypads have keys mapped with **distinct** collections of lowercase English letters, which can be used to form words by pushing them. For example, the key `2` is mapped with `["a","b","c"]`, where you need to push the key:
- one time to type "a",
- two times to type "b", 
- three times to type "c".

It is allowed to remap the keys numbered `2` to `9` to **distinct** collections of letters. The keys can be remapped to **any** amount of letters, but each letter **must** be mapped to **exactly** one key. You need to find the **minimum** number of times the keys will be pushed to type the string `word`.

Return *the **minimum** number of pushes needed to type `word` after remapping the keys*.

**Constraints:**
- `1 <= word.length <= 10^5`
- `word` consists of lowercase English letters.

## Solution

**Understanding the Problem:**
   - We need to determine the minimum number of key presses required to type a given string `word` on a remapped telephone keypad.
   - Each letter in the string must be mapped to exactly one key on the keypad.
   - Our task is to minimize the total number of key presses by optimally remapping the keys.

**Breaking It Down**
   - **Mapping Strategy:**
     - We need to map the most frequently occurring letters in `word` to keys that require the fewest presses.
     - The optimal mapping would assign the most frequent letters to positions where they can be typed with fewer key presses (i.e., first or second positions on a key).
     
   - **Greedy Approach:**
     - Count the frequency of each letter in `word`.
     - Sort the letters based on frequency in descending order.
     - Assign the most frequent letters to the positions on keys that require fewer presses, starting from the key `2`.

**Implementation Approach:**
   - Count the frequency of each letter in `word`.
   - Sort the letters based on frequency, with the most frequent letters first.
   - Assign these letters to the keypad keys, starting from the position with the least number of presses (first position of key `2`).
   - Calculate the total number of key presses needed to type `word`.

**Algorithm Steps:**
   - **Count Frequencies:** Create a frequency map of the letters in `word`.
   - **Sort by Frequency:** Sort the letters based on their frequency in descending order.
   - **Assign Keys:** Assign letters to keypad positions starting from the one that requires the fewest presses.
   - **Calculate Total Presses:** Compute the total number of key presses needed for the entire `word` using the assigned mapping.

### Python Code

```python
class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        
```

### Example

```python
# Input
word = "hello"

# Output
8
```

### Explanation
1. **Frequency Count:** 
   - `h`: 1
   - `e`: 1
   - `l`: 2
   - `o`: 1
2. **Optimal Mapping:**
   - Assign 'l' to the first position on key `2`, 'h', 'e', and 'o' to other keys.
3. **Total Presses:** `1*2 + 1*1 + 2*1 + 1*1 + 1*1 = 8`.

### Usage

To use the solution, create an instance of the `Solution` class and call the `minimumPushes` method with the `word` string:

```python
# Example usage
solution = Solution()
word = "hello"
result = solution.minimumPushes(word)
print(result)  # Output: 8
```

### Additional Resources

[Link to detailed explanation on Algo Monster](https://algo.monster/liteproblems/3016)

[Link to detailed explanation on Medium](https://medium.com/@ganjooshreya5/weekly-contest-381-3016-minimum-number-of-pushes-to-type-word-ii-0b177404c9f4)


### Check Out These Video(s)

[![Video Explanation](https://img.youtube.com/vi/xhi_c7JdDkM/mqdefault.jpg)](https://youtu.be/xhi_c7JdDkM)

[![Video Explanation](https://img.youtube.com/vi/gvaYi6X6SQw/mqdefault.jpg)](https://youtu.be/gvaYi6X6SQw)

### Complexity Analysis

- **Time Complexity:** O(n log n), where `n` is the length of the string `word`. Sorting the frequencies is the most time-consuming operation.
- **Space Complexity:** O(1), as we are only using a few extra variables beyond the input size.