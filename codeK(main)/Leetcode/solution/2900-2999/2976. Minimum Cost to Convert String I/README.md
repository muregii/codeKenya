# Leetcode - Minimum Cost to Convert String

## Problem Description

You are given two **0-indexed** strings `source` and `target`, both of length `n` and consisting of **lowercase** English letters. You are also given two **0-indexed** character arrays `original` and `changed`, and an integer array `cost`, where `cost[i]` represents the cost of changing the character `original[i]` to the character `changed[i]`.

You start with the string `source`. In one operation, you can pick a character `x` from the string and change it to the character `y` at a cost of `z` if there exists any index `j` such that `cost[j] == z`, `original[j] == x`, and `changed[j] == y`.

Return *the **minimum** cost to convert the string `source` to the string `target` using **any** number of operations. If it is impossible to convert `source` to `target`, return `-1`*.

**Note:** There may exist indices `i`, `j` such that `original[j] == original[i]` and `changed[j] == changed[i]`.

**Constraints:**
- `1 <= source.length == target.length <= 10^5`
- `source, target` consist of lowercase English letters.
- `1 <= cost.length == original.length == changed.length <= 2000`
- `original[i], changed[i]` are lowercase English letters.
- `1 <= cost[i] <= 10^6`
- `original[i] != changed[i]`

## Solution

**Understanding the Problem:**
   - We have two strings, `source` and `target`, and we need to transform `source` into `target`.
   - The transformation is controlled by the `original`, `changed`, and `cost` arrays, which dictate the possible character changes and their associated costs.
   - The goal is to find the minimum total cost to make `source` identical to `target`, or determine if it's impossible.

**Breaking It Down**
   - **Mapping Character Changes:**
     First, we need to understand the allowed transformations. The `original` and `changed` arrays give us the pairs of characters we can change, while the `cost` array provides the cost for each transformation.
     
   - **Dynamic Programming Approach:**
     - We can use dynamic programming (DP) to track the minimum cost to convert each character in `source` to its corresponding character in `target`.
     - The DP approach involves iterating through each character in `source` and checking if it can be transformed into the corresponding character in `target` using the given transformations.
     
   - **Impossible Transformations:**
     - If at any point a required transformation isn't possible (i.e., there's no corresponding entry in `original` and `changed` for a particular transformation), then the conversion is impossible, and we return `-1`.

**Implementation Approach:**
   - Create a dictionary to map each character in `original` to its possible transformations in `changed` with the associated costs.
   - Iterate through each character in `source` and use the dictionary to calculate the minimum cost required to transform it into the corresponding character in `target`.
   - Accumulate the total cost and return it if all transformations are possible. Otherwise, return `-1`.

**Algorithm Steps:**
   - **Build a Transformation Map:** Create a dictionary that maps each character in `original` to the possible characters it can be changed into, along with the corresponding costs.
   - **Iterate Through Source:** For each character in `source`, determine the minimum cost to change it to the corresponding character in `target`.
   - **Calculate the Total Cost:** Sum up the costs for each character transformation.
   - **Check Feasibility:** If any transformation is impossible, return `-1`.

### Python Code

```python
class Solution(object):
    def minimumCost(self, source, target, original, changed, cost):
        """
        :type source: str
        :type target: str
        :type original: List[str]
        :type changed: List[str]
        :type cost: List[int]
        :rtype: int
        """
        
```

### Example

```python
# Input
source = "abc"
target = "bcd"
original = ['a', 'b', 'c']
changed = ['b', 'c', 'd']
cost = [1, 2, 3]

# Output
6
```

### Explanation
1. **Transformation Map:** Create a mapping for transformations: `{'a': [('b', 1)], 'b': [('c', 2)], 'c': [('d', 3)]}`.
2. **Iterate Through Source:** Calculate the minimum cost for each character transformation in `source` to match `target`.
3. **Result:** The minimum cost to transform "abc" into "bcd" is `1 (a->b) + 2 (b->c) + 3 (c->d) = 6`.

### Usage

To use the solution, create an instance of the `Solution` class and call the `minimumCost` method with the `source`, `target`, `original`, `changed`, and `cost` arrays:

```python
# Example usage
solution = Solution()
source = "abc"
target = "bcd"
original = ['a', 'b', 'c']
changed = ['b', 'c', 'd']
cost = [1, 2, 3]
result = solution.minimumCost(source, target, original, changed, cost)
print(result)  # Output: 6
```

### Additional Resources

[Link to detailed explanation on Algo Monster](https://algo.monster/liteproblems/2976)

[Link to detailed explanation on Geeksforgeeks](https://www.geeksforgeeks.org/minimum-cost-to-convert-given-string-to-consist-of-only-vowels/)

[Link to detailed explanation on Medium](https://yash-soni.medium.com/solving-the-minimum-cost-to-convert-string-problem-efficiently-693d488c4a41)

[Link to detailed explanation on Geeksforgeeks](https://www.geeksforgeeks.org/minimum-cost-to-convert-one-given-string-to-another-using-swap-insert-or-delete-operations/)

### Check Out These Video(s)

[![Video Explanation](https://img.youtube.com/vi/AVJhazQsNms/mqdefault.jpg)](https://youtu.be/AVJhazQsNms)

### Complexity Analysis

- **Time Complexity:** O(n * m), where `n` is the length of the `source` string and `m` is the number of transformations available.
- **Space Complexity:** O(m), for storing the transformation map.