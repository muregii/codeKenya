# Leetcode - Maximum Value Sum of Tree Nodes

## Problem Description

There exists an **undirected** tree with `n` nodes numbered `0` to `n - 1`. You are given a **0-indexed** 2D integer array `edges` of length `n - 1`, where `edges[i] = [ui, vi]` indicates that there is an edge between nodes `ui` and `vi` in the tree. You are also given a positive integer `k`, and a **0-indexed** array of **non-negative** integers `nums` of length `n`, where `nums[i]` represents the value of the node numbered `i`.

Alice wants the sum of values of tree nodes to be **maximum**, for which Alice can perform the following operation **any** number of times (**including zero**) on the tree:

Choose any edge `[u, v]` connecting the nodes `u` and `v`, and update their values as follows:
- `nums[u] = nums[u] XOR k`
- `nums[v] = nums[v] XOR k`

Return *the **maximum** possible **sum** of the **values** Alice can achieve by performing the operation **any** number of times.*

**Constraints:**
- `2 <= n == nums.length <= 2 * 10^4`
- `1 <= k <= 10^9`
- `0 <= nums[i] <= 10^9`
- `edges.length == n - 1`
- `edges[i].length == 2`
- `0 <= edges[i][0], edges[i][1] <= n - 1`
- The input is generated such that `edges` represent a valid tree.

## Solution

Maximize the sum of the values of tree nodes by applying the XOR operation on the nodes connected by edges any number of times.

Think of a tree where each branch has some number of apples. We want to collect as many apples as possible. We have a magic number, and if we shake a branch, the number of apples on both ends of the branch will change. We can shake any branch as many times as we want to get the most apples.



The `maximumValueSum` method takes the values of the nodes (`nums`), the magic number (`k`), and the edges of the tree (`edges`) as input. The goal is to maximize the sum of the values of the nodes.

1. **Understanding XOR Operation:**
   - The XOR operation is a bitwise operation that flips the bits of a number. If we XOR a number with `k`, it changes the number to a different value. Applying XOR again with the same `k` reverts it back to the original value.
   
2. **Maximizing Node Values:**
   - To maximize the sum of the values, we need to consider applying the XOR operation on all edges. We should explore the possibility of XORing each node's value with `k` to see if it increases the total sum.

3. **Algorithm:**
   - Traverse each node and calculate the sum of values if we XOR each node value with `k`.
   - Compare the original sum with the sum obtained after XORing with `k`.
   - Return the maximum sum obtained.


We have a tree with nodes that have certain values. We want to maximize the total sum of these values by using a special operation (XOR) on the nodes connected by edges. The XOR operation changes the value of the nodes. We check if applying XOR gives us a higher total sum and return the highest possible sum.


```python
class Solution(object):
    def maximumValueSum(self, nums, k, edges):
        """
        :type nums: List[int]
        :type k: int
        :type edges: List[List[int]]
        :rtype: int
        """
```

## Usage

To use the solution, create an instance of the `Solution` class and call the `maximumValueSum` method with the values of the nodes, the magic number `k`, and the edges of the tree:

```python
solution = Solution()
nums = [1, 2, 3]
k = 2
edges = [[0, 1], [1, 2]]
result = solution.maximumValueSum(nums, k, edges)
print(result)  # Output: 6
```

[Link to detailed explanation on Medium](https://medium.com/basecs/breaking-down-breadth-first-search-cebe696709d9)

[Link to detailed explanation on Medium](https://yash-soni.medium.com/solving-leetcode-3068-find-the-maximum-sum-of-node-values-4817bed75282)

[Link to detailed explanation on Geeksforgeeks](https://www.geeksforgeeks.org/maximum-sum-of-values-of-nodes-among-all-connected-components-of-an-undirected-graph/)


## Check Out this videos

[![Video Explanation](https://img.youtube.com/vi/bnBp6_b4GCw/mqdefault.jpg)](https://youtu.be/bnBp6_b4GCw)

[![Video Explanation](https://img.youtube.com/vi/3t7y4mBJDoM/mqdefault.jpg)](https://youtu.be/3t7y4mBJDoM)

[![Video Explanation](https://img.youtube.com/vi/34l1kTIQCIA/mqdefault.jpg)](https://youtu.be/34l1kTIQCIA)

## Complexity Analysis

- **Time Complexity:** O(n), where n is the number of nodes. We traverse all nodes once to calculate the sums.
- **Space Complexity:** O(1), as we are using a constant amount of extra space for calculations.
