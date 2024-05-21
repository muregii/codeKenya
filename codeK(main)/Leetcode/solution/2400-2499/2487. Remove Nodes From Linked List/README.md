# Leetcode - Remove Nodes From Linked List

## Problem Description

You are given the `head` of a linked list.

Remove every node which has a node with a greater value anywhere to the right side of it.

Return *the `head` of the modified linked list.*

**Custom testing:**

- For the input, you should provide the entire linked list `head`.
- The output will be the entire list after calling your function.

## Solution

To solve this problem, we can reverse the linked list and use a greedy approach to keep track of the maximum value seen so far. We only keep nodes that are greater than or equal to this maximum value.

Here's how we can approach this problem:

1. Reverse the linked list.
2. Initialize `max_val` to the value of the first node.
3. Traverse the reversed list:
   - If the current node's value is greater than or equal to `max_val`, update `max_val` and move to the next node.
   - If the current node's value is less than `max_val`, remove the current node.
4. Reverse the list again to restore the original order but with the desired nodes removed.
5. Return the head of the modified list.

By reversing the list, we ensure that we can traverse from the rightmost node to the leftmost node, allowing us to keep track of the maximum value efficiently.

## Usage

To use the solution, create an instance of the `Solution` class and call the `removeNodes` method with the input parameter `head`:

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
```

```python
# Example linked list before removal: 5 -> 2 -> 13 -> 3 -> 8
# After removal: 13 -> 8
```

[Link to detailed explanation on Geeksforgeeks](https://www.geeksforgeeks.org/remove-first-node-of-the-linked-list/)

[Link to detailed explanation on Medium](https://medium.com/nerd-for-tech/leetcode-remove-nodes-from-linked-list-f5f824c5896e)

[Link to detailed explanation on Geeksforgeeks](https://www.geeksforgeeks.org/remove-last-node-of-the-linked-list/)

[Link to detailed explanation on Geeksforgeeks](https://www.geeksforgeeks.org/deletion-in-linked-list/)

[Link to detailed explanation on Medium](https://medium.com/@Neelesh-Janga/q-203-leetcode-removing-nodes-with-a-specific-value-from-a-linked-list-ec848c5a6997)

[Link to detailed explanation on Code Academy](https://www.codecademy.com/article/doubly-linked-list-conceptual)

## Check Out this video

[![Video Explanation](https://img.youtube.com/vi/nfVoWfBNBHU/mqdefault.jpg)](https://youtu.be/nfVoWfBNBHU)


[![Video Explanation](https://img.youtube.com/vi/YAn_wn2YLQ8/mqdefault.jpg)](https://youtu.be/YAn_wn2YLQ8)


[![Video Explanation](https://img.youtube.com/vi/IGqowY9tjpw/mqdefault.jpg)](https://youtu.be/IGqowY9tjpw)


[![Video Explanation](https://img.youtube.com/vi/y783sRTezDg/mqdefault.jpg)](https://youtu.be/y783sRTezDg)


## Complexity Analysis

- **Time Complexity:** O(n), where n is the number of nodes in the linked list. We traverse the list three times (reverse, traverse, and reverse again).
- **Space Complexity:** O(1). We use only constant extra space for pointers and variables.