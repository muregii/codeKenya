# Leetcode - Kth Distinct String in an Array

## Problem Description

A **distinct string** is a string that is present only **once** in an array.

Given an array of strings `arr`, and an integer `k`, return *the `k`th distinct string present in `arr`*. If there are **fewer** than `k` distinct strings, return *an empty string* `""`.

Note that the strings are considered in the **order in which they appear** in the array.

**Constraints:**
- `1 <= k <= arr.length <= 1000`
- `1 <= arr[i].length <= 5`
- `arr[i]` consists of lowercase English letters.

## Solution

**Understanding the Problem:**
   - We are given an array of strings `arr` and need to find the `k`th distinct string.
   - A distinct string is one that appears only once in the array.
   - If there are fewer than `k` distinct strings, we should return an empty string `""`.

**Breaking It Down**
   - **Counting Frequencies:**
     - We need to count the frequency of each string in the array. This will help us identify which strings are distinct (appear only once).
     
   - **Finding the Kth Distinct String:**
     - After counting the frequencies, we traverse the array again in the given order to identify the distinct strings.
     - We stop when we find the `k`th distinct string.

**Implementation Approach:**
   - Use a dictionary to count the occurrences of each string in `arr`.
   - Iterate through `arr` again to find the `k`th string that has a frequency of `1`.
   - If we find the `k`th distinct string, return it; otherwise, return an empty string `""`.

**Algorithm Steps:**
   - **Count Frequencies:** Traverse the array `arr` and count how many times each string appears using a dictionary.
   - **Identify Distinct Strings:** Traverse `arr` again, checking the frequency of each string in the dictionary.
   - **Return the Result:** When the `k`th distinct string is found, return it; if there are fewer than `k` distinct strings, return an empty string.

### Python Code

```python
class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        
```

### Example

```python
# Input
arr = ["a", "b", "a", "c", "b", "d"]
k = 2

# Output
"d"
```

### Explanation
1. **Counting Frequencies:** 
   - `a` appears 2 times, 
   - `b` appears 2 times, 
   - `c` appears 1 time, 
   - `d` appears 1 time.
2. **Finding the 2nd Distinct String:**
   - The distinct strings in order are `["c", "d"]`.
   - The 2nd distinct string is `"d"`.

### Usage

To use the solution, create an instance of the `Solution` class and call the `kthDistinct` method with the `arr` and `k` parameters:

```python
# Example usage
solution = Solution()
arr = ["a", "b", "a", "c", "b", "d"]
k = 2
result = solution.kthDistinct(arr, k)
print(result)  # Output: "d"
```

### Additional Resources

[Link to detailed explanation on Algo Monster](https://algo.monster/liteproblems/2053)

[Link to detailed explanation on Geeksforgeeks](https://www.geeksforgeeks.org/find-kth-distinct-character-from-start-of-given-given-string/)


### Check Out These Video(s)

[![Video Explanation](https://img.youtube.com/vi/1KOnvGPv9Mo/mqdefault.jpg)](https://youtu.be/1KOnvGPv9Mo)

### Complexity Analysis

- **Time Complexity:** O(n), where `n` is the length of the array `arr`. We traverse the array twice.
- **Space Complexity:** O(n), for storing the frequency count of each string in a dictionary.