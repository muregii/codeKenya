# Leetcode - Sort the People

## Problem Description

You are given an array of strings `names`, and an array `heights` that consists of **distinct** positive integers. Both arrays are of length `n`.

For each index `i`, `names[i]` and `heights[i]` denote the name and height of the `i^th` person.

Return *`names` sorted in **descending** order by the people's heights*.

**Constraints:**
- `n == names.length == heights.length`
- `1 <= n <= 10^3`
- `1 <= names[i].length <= 20`
- `1 <= heights[i] <= 10^5`
- `names[i]` consists of lower and upper case English letters.
- All the values in `heights` are distinct.

## Solution

**Understanding the Problem:**
   - We are given a list of people, with each person represented by their name and height.
   - The goal is to rearrange the names of the people based on their heights, from the tallest to the shortest.
   - Since all heights are distinct, we can sort the people directly by height and return the corresponding sorted names.

**Breaking It Down**
   - **Organizing the Data.** 
     We are given two arrays: `names` and `heights`. The index `i` in both arrays corresponds to the same person.
     
   - **Sorting the Data.**
     To sort people by height in descending order, we need to:
     1. Combine `names` and `heights` into a list of tuples.
     2. Sort this list based on the heights (in descending order).
     3. Extract and return only the names in the new sorted order.
     
   - **Implementation Approach.**
     We can zip the two lists together to form pairs of `(name, height)` for each person, then sort them by the second element (height) in reverse order. Finally, extract the names and return them in the sorted order.

**Algorithm Steps:**
   - Create pairs of `(name, height)` using Python's `zip` function.
   - Sort the list of pairs based on the height in descending order.
   - Extract and return the names from the sorted list of pairs.

### Python Code

```python
class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        
```

### Example

```python
# Input
names = ["Alice", "Bob", "Charlie"]
heights = [155, 185, 150]

# Output
["Bob", "Alice", "Charlie"]
```

### Explanation
1. Combine the names and heights into a list of pairs: `[(155, "Alice"), (185, "Bob"), (150, "Charlie")]`.
2. Sort by heights in descending order: `[(185, "Bob"), (155, "Alice"), (150, "Charlie")]`.
3. Extract the sorted names: `["Bob", "Alice", "Charlie"]`.

### Usage

To use the solution, create an instance of the `Solution` class and call the `sortPeople` method with the `names` and `heights` arrays:

```python
# Example usage
solution = Solution()
names = ["Alice", "Bob", "Charlie"]
heights = [155, 185, 150]
sorted_names = solution.sortPeople(names, heights)
print(sorted_names)  # Output: ["Bob", "Alice", "Charlie"]
```


### Additional Resources

[Link to detailed explanation on Algo Monster](https://algo.monster/liteproblems/2418)

[Link to detailed explanation on Medium](https://medium.com/@safaizalways/the-explanation-for-the-leetcode-problem-no-2418-b2583e05b22f)

### Check Out These Video(s)

[![Video Explanation](https://img.youtube.com/vi/1hq5k_I6TqY/mqdefault.jpg)](https://youtu.be/1hq5k_I6TqY)

[![Video Explanation](https://img.youtube.com/vi/CC3xtYipI_8/mqdefault.jpg)](https://youtu.be/CC3xtYipI_8)

[![Video Explanation](https://img.youtube.com/vi/Zv_gXqqslbw/mqdefault.jpg)](https://youtu.be/Zv_gXqqslbw)


### Complexity Analysis

- **Time Complexity:** O(n log n), where `n` is the length of the arrays. The sorting step takes `O(n log n)`, and zipping the arrays and extracting names takes linear time.
- **Space Complexity:** O(n), for storing the sorted list of tuples and the result array.