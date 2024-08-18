# Leetcode - Second Minimum Time to Reach Destination

## Problem Description

A city is represented as a **bi-directional** connected graph with `n` vertices where each vertex is labeled from `1` to `n` (**inclusive**). The edges in the graph are represented as a 2D integer array `edges`, where each `edges[i] = [u^i, v^i]` denotes a bi-directional edge between vertex `u^i` and vertex `v^i`. Every vertex pair is connected by **at most one** edge, and no vertex has an edge to itself. The time taken to traverse any edge is `time` minutes.

Each vertex has a traffic signal which changes its color from **green** to **red** and vice versa every `change` minutes. All signals change **at the same time**. You can enter a vertex at **any time**, but can leave a vertex** only when the signal is green**. You **cannot wait** at a vertex if the signal is **green**.

The **second minimum value** is defined as the smallest value **strictly larger** than the minimum value.

- For example the second minimum value of `[2, 3, 4]` is `3`, and the second minimum value of `[2, 2, 4]` is `4`.

Given `n`, `edges`, `time`, and `change`, return *the **second minimum time** it will take to go from vertex `1` to vertex `n`.*

**Notes:**
- You can go through any vertex **any** number of times, **including** `1` and `n`.
- You can assume that when the journey **starts**, all signals have just turned **green**.

**Constraints:**
- `2 <= n <= 10^4`
- `n - 1 <= edges.length <= min(2 * 10^4, n * (n - 1) / 2)`
- `edges[i].length == 2`
- `1 <= ui, vi <= n`
- `ui != vi`
- There are no duplicate edges.
- Each vertex can be reached directly or indirectly from every other vertex.
- `1 <= time, change <= 10^3`

## Solution

**Understanding the Problem:**
   - We are given a graph representing a city with traffic signals that alternate between green and red every `change` minutes.
   - The goal is to find the second minimum time it takes to travel from vertex `1` to vertex `n`, considering the traffic signals' timing constraints.

**Breaking It Down**
   - **Graph Traversal with Constraints:**
     To solve this problem, we need to traverse the graph while considering the traffic signals' timing at each vertex. This adds complexity because we can't leave a vertex unless the signal is green.
     
   - **Finding the Second Minimum Time:**
     - The first task is to determine the minimum time to reach the destination.
     - The second task is to continue the search to find the second minimum time, which is the next smallest time greater than the minimum.

**Implementation Approach:**
   - **Breadth-First Search (BFS):** We can use BFS to explore all possible paths from vertex `1` to vertex `n`.
   - **Time Management:** For each step, we need to calculate the time considering the traffic signal's state (green or red) at the destination vertex.
   - **Tracking Times:** We maintain a list of the two smallest times to reach vertex `n` and return the second minimum time.

**Algorithm Steps:**
   - **Initialize BFS:** Start BFS from vertex `1`, keeping track of time and signal states.
   - **Explore Paths:** At each vertex, calculate the time to move to adjacent vertices, considering whether the signal is green or red when you arrive.
   - **Track Minimum and Second Minimum Times:** Update the smallest and second smallest times to reach vertex `n`.
   - **Return the Second Minimum:** Once BFS completes, return the second minimum time.

### Python Code

```python
class Solution(object):
    def secondMinimum(self, n, edges, time, change):
        """
        :type n: int
        :type edges: List[List[int]]
        :type time: int
        :type change: int
        :rtype: int
        """
        
```

### Example

```python
# Input
n = 5
edges = [[1,2],[1,3],[1,4],[3,4],[4,5]]
time = 3
change = 5

# Output
13
```

### Explanation
1. **Graph Representation:** The city is represented as a graph with vertices and bi-directional edges.
2. **BFS Traversal:** Using BFS, we explore all paths considering traffic signal constraints.
3. **Second Minimum Time:** After finding the minimum time to reach vertex `n`, the BFS continues to find the second minimum time, which is `13` in this case.

### Usage

To use the solution, create an instance of the `Solution` class and call the `secondMinimum` method with the `n`, `edges`, `time`, and `change` parameters:

```python
# Example usage
solution = Solution()
n = 5
edges = [[1,2],[1,3],[1,4],[3,4],[4,5]]
time = 3
change = 5
result = solution.secondMinimum(n, edges, time, change)
print(result)  # Output: 13
```

### Additional Resources

[Link to detailed explanation on Algo Monster](https://algo.monster/liteproblems/2045)

[Link to detailed explanation on Geeksforgeeks](https://www.geeksforgeeks.org/number-of-ways-to-reach-at-destination-in-shortest-time/)

[Link to detailed explanation on Geeksforgeeks](https://www.geeksforgeeks.org/minimum-positive-points-to-reach-destination/)

[Link to detailed explanation on Geeksforgeeks](https://www.geeksforgeeks.org/minimum-steps-to-reach-a-destination/)

### Check Out These Video(s)

[![Video Explanation](https://img.youtube.com/vi/BPCT3TmOKGo/mqdefault.jpg)](https://youtu.be/BPCT3TmOKGo)

[![Video Explanation](https://img.youtube.com/vi/ck3KrlaNch4/mqdefault.jpg)](https://youtu.be/ck3KrlaNch4)

[![Video Explanation](https://img.youtube.com/vi/2F7gwxfy1CU/mqdefault.jpg)](https://youtu.be/2F7gwxfy1CU)

### Complexity Analysis

- **Time Complexity:** O(n + m), where `n` is the number of vertices and `m` is the number of edges.
- **Space Complexity:** O(n + m), for storing the graph and BFS queue.