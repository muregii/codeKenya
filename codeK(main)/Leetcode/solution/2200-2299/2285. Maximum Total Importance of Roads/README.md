# Leetcode - Maximum Total Importance of Roads

## Problem Description

You are given an integer `n` denoting the number of cities in a country. The cities are numbered from `0` to `n - 1`.

You are also given a 2D integer array `roads` where `roads[i] = [ai, bi]` denotes that there exists a **bidirectional** road connecting cities `ai` and `bi`.

You need to assign each city with an integer value from `1` to `n`, where each value can only be used **once**. The **importance** of a road is then defined as the sum of the values of the two cities it connects.

Return *the **maximum total importance** of all roads possible after assigning the values optimally*.

**Constraints:**
- `2 <= n <= 5 * 10^4`
- `1 <= roads.length <= 5 * 10^4`
- `roads[i].length == 2`
- `0 <= ai, bi <= n - 1`
- `ai != bi`
- There are no duplicate roads.

## Solution

To maximize the total importance of all roads, assign higher values to the most connected cities. This ensures that roads connecting these cities contribute more to the total importance.

1. **Understanding the Problem:**
   - We need to maximize the total importance of roads by optimally assigning values to cities.
   - The importance of a road is the sum of the values of the two cities it connects.
   - Assign higher values to cities with more connections.

2. **Using Degree Counting:**
   - Calculate the degree (number of connections) of each city.
   - Assign values to cities based on their degree, giving the highest value to the city with the highest degree, and so on.

3. **Algorithm Steps:**
   - Calculate the degree of each city.
   - Sort the cities based on their degree in descending order.
   - Assign values from `n` to `1` based on the sorted order.
   - Calculate the total importance of all roads using the assigned values.

### Example

Suppose you have the following cities and roads:

```
n = 4
roads = [[0, 1], [0, 2], [1, 2], [1, 3]]
```

- Calculate degrees:
  - City 0: 2 roads
  - City 1: 3 roads
  - City 2: 2 roads
  - City 3: 1 road

- Assign values based on degree:
  - City 1: 4 (highest degree)
  - City 0: 3
  - City 2: 2
  - City 3: 1

- Total importance:
  - Road [0, 1]: 3 + 4 = 7
  - Road [0, 2]: 3 + 2 = 5
  - Road [1, 2]: 4 + 2 = 6
  - Road [1, 3]: 4 + 1 = 5

Total importance = 7 + 5 + 6 + 5 = 23

### Python Code

```python
class Solution(object):
    def maximumImportance(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        
```

### Usage

To use the solution, create an instance of the `Solution` class and call the `maximumImportance` method with the number of cities and the `roads` array:

```python
solution = Solution()
n = 4
roads = [[0, 1], [0, 2], [1, 2], [1, 3]]
result = solution.maximumImportance(n, roads)
print(result)  # Output: 23
```

### Additional Resources

[Link to detailed explanation on Algo Monster](https://algo.monster/liteproblems/2285)

[Link to detailed explanation on Medium](https://medium.com/@okesseko/leetcode-day58-2285-ebe11b9ecc88)

### Check Out These Videos

[![Video Explanation](https://img.youtube.com/vi/NIhXLEiQAPM/mqdefault.jpg)](https://youtu.be/NIhXLEiQAPM)

[![Video Explanation](https://img.youtube.com/vi/BU3fuEVSavs/mqdefault.jpg)](https://youtu.be/BU3fuEVSavs)

### Complexity Analysis

- **Time Complexity:** O(n + m log n), where `n` is the number of cities and `m` is the number of roads. Sorting the cities takes `O(n log n)`, and calculating the degrees and the total importance takes `O(n + m)`.
- **Space Complexity:** O(n), for storing the degree and value mappings.