# Leetcode - Find the Minimum and Maximum Number of Nodes Between Critical Points

## Problem Description

A **critical point** in a linked list is defined as **either** a **local maxima** or a **local minima**.

- A node is a **local maxima** if the current node has a value **strictly greater** than the previous node and the next node.
- A node is a **local minima** if the current node has a value **strictly smaller** than the previous node and the next node.

Note that a node can only be a local maxima/minima if there exists **both** a previous node and a next node.

Given a linked list `head`, *return an array of length 2 containing `[minDistance, maxDistance]` where `minDistance` is the **minimum distance** between any **two distinct** critical points and `maxDistance` is the **maximum distance** between **any two distinc**t critical points. If there are **fewer** than two critical points, return `[-1, -1]`*.

**Constraints:**
- The number of nodes in the list is **in the range** [2, 10^5].
- `1 <= Node.val <= 10^5`

## Solution

To find the minimum and maximum distance between critical points, traverse the linked list, identify critical points, and then calculate the distances between them.

1. **Understanding the Problem:**
   - Identify nodes that are local maxima or local minima.
   - Calculate the minimum and maximum distances between these critical points.
   - Return `[-1, -1]` if there are fewer than two critical points.

2. **Traversing the Linked List:**
   - Use pointers to keep track of the previous, current, and next nodes.
   - Identify and record the positions of critical points.
   - Calculate the minimum and maximum distances between the recorded positions.

3. **Algorithm Steps:**
   - Initialize pointers to traverse the list and a list to store critical point positions.
   - Traverse the list, identifying critical points and recording their positions.
   - If fewer than two critical points are found, return `[-1, -1]`.
   - Calculate the minimum and maximum distances between the critical points.
   - Return the distances as `[minDistance, maxDistance]`.

### Example

Suppose you have the following linked list:

```
5 -> 3 -> 1 -> 3 -> 7 -> 5
```

- Traverse the list to find critical points:
  - At position 1: 3 (local minima)
  - At position 3: 3 (local maxima)
  - At position 4: 7 (local maxima)

- Calculate distances:
  - Minimum distance: `2` (between positions 1 and 3)
  - Maximum distance: `3` (between positions 1 and 4)

- The result is `[2, 3]`.

### Python Code

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        
```

### Usage

To use the solution, create an instance of the `Solution` class and call the `nodesBetweenCriticalPoints` method with the head of the linked list:

```python
# Helper function to create linked list from a list of values
def create_linked_list(vals):
    head = ListNode(vals[0])
    current = head
    for val in vals[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Example usage
solution = Solution()
head = create_linked_list([5, 3, 1, 3, 7, 5])
result = solution.nodesBetweenCriticalPoints(head)
print(result)  # Output: [2, 3]
```

### Additional Resources

[Link to detailed explanation on Algo Monster](https://algo.monster/liteproblems/2058)

[Link to detailed explanation on Medium](https://medium.com/@hongjje.dev/leetcode-solution-2058-find-the-minimum-and-maximum-number-of-nodes-between-critical-points-3db43399ca1a)

[Link to detailed explanation on Geeksforgeeks](https://www.geeksforgeeks.org/minimum-and-maximum-number-of-nodes-between-critical-points/)

### Check Out These Videos

[![Video Explanation](https://img.youtube.com/vi/cuUk_JMQc1E/mqdefault.jpg)](https://youtu.be/cuUk_JMQc1E)

[![Video Explanation](https://img.youtube.com/vi/hfNQl_iEtvs/mqdefault.jpg)](https://youtu.be/hfNQl_iEtvs)

[![Video Explanation](https://img.youtube.com/vi/UddDgt52h9g/mqdefault.jpg)](https://youtu.be/UddDgt52h9g)

### Complexity Analysis

- **Time Complexity:** O(n), where `n` is the number of nodes in the linked list. We traverse the list once.
- **Space Complexity:** O(1), as we only use a constant amount of extra space beyond the input list for storing the critical point positions.
