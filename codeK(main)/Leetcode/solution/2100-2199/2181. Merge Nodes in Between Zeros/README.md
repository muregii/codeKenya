# Leetcode - Merge Nodes in Between Zeros

## Problem Description

You are given the head of a linked list, which contains a series of integers **separated** by `0`'s. The **beginning** and **end** of the linked list will have `Node.val == 0`.

For **every** two consecutive `0`'s, merge all the nodes lying in between them into a single node whose value is the **sum** of all the merged nodes. The modified list should not contain any `0`'s.

Return *the `head` of the modified linked list*.

**Constraints:**
- The number of nodes in the list is in the range [3, 2 * 10^5].
- `0 <= Node.val <= 1000`
- There are **no** two consecutive nodes with `Node.val == 0`.
- The **beginning** and **end** of the linked list have `Node.val == 0`.

## Solution

To merge nodes in between zeros, traverse the linked list and sum the values between each pair of zeros, creating new nodes with these sums and forming the new linked list without zeros.

1. **Understanding the Problem:**
   - Merge nodes between every two consecutive zeros.
   - Each resulting node should hold the sum of the merged nodes.
   - The new list should not contain any zeros.

2. **Traversing the Linked List:**
   - Use a pointer to traverse the linked list.
   - Accumulate the values between zeros.
   - Create new nodes with the accumulated sum and link them to form the new list.

3. **Algorithm Steps:**
   - Initialize a dummy node to help build the new list.
   - Use a pointer to traverse the list and a variable to accumulate sums.
   - When a zero is encountered, if the accumulated sum is non-zero, create a new node and reset the sum.
   - Continue until the end of the list, then return the next of the dummy node, which is the head of the new list.

### Example

Suppose you have the following linked list:

```
0 -> 3 -> 1 -> 0 -> 4 -> 5 -> 2 -> 0
```

- Initialize a dummy node.
- Traverse the list and accumulate sums:
  - Encounter 0, skip.
  - Accumulate: 3 + 1 = 4
  - Encounter 0, create new node with sum 4.
  - Accumulate: 4 + 5 + 2 = 11
  - Encounter 0, create new node with sum 11.
  
- The modified list is:

```
4 -> 11
```

### Python Code

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
```

### Usage

To use the solution, create an instance of the `Solution` class and call the `mergeNodes` method with the head of the linked list:

```python
# Helper function to create linked list from a list of values
def create_linked_list(vals):
    head = ListNode(vals[0])
    current = head
    for val in vals[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print linked list
def print_linked_list(head):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    print(" -> ".join(map(str, vals)))

solution = Solution()
head = create_linked_list([0, 3, 1, 0, 4, 5, 2, 0])
result = solution.mergeNodes(head)
print_linked_list(result)  # Output: 4 -> 11
```

### Additional Resources

[Link to detailed explanation on Algo Monster](https://algo.monster/liteproblems/2181)

[Link to detailed explanation on Medium](https://medium.com/@1chooo/leetcode-2181-merge-nodes-in-between-zeros-go-8a4ff44140cc)

[Link to detailed explanation on Geeksforgeeks](https://www.geeksforgeeks.org/linked-list-sum-nodes-0s/)

### Check Out These Videos

[![Video Explanation](https://img.youtube.com/vi/jrSav7fulJY/mqdefault.jpg)](https://youtu.be/jrSav7fulJY)

[![Video Explanation](https://img.youtube.com/vi/SOY3c6yzzwk/mqdefault.jpg)](https://youtu.be/SOY3c6yzzwk)

### Complexity Analysis

- **Time Complexity:** O(n), where `n` is the number of nodes in the linked list. We traverse the list once.
- **Space Complexity:** O(1), as we only use a constant amount of extra space beyond the input list.