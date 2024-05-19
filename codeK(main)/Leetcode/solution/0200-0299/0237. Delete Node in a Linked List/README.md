# Leetcode - Delete Node in a Linked List

## Problem Description

There is a singly-linked list `head` and we want to delete a node `node` in it.

You are given the node to be deleted `node`. You will **not be given access** to the first node of `head`.

All the values of the linked list are **unique**, and it is guaranteed that the given `node` is not the last node in the linked list.

Delete the given `node`. Note that by deleting the node, we do not mean removing it from memory. We mean:

- The value of the given `node` should not exist in the linked list.
- The number of nodes in the linked list should decrease by one.
- All the values before `node` should be in the same order.
- All the values after `node` should be in the same order.

**Custom testing:**

- For the input, you should provide the entire linked list `head` and the node to be given `node`. `node` should not be the last node of the list and should be an actual node in the list.
- We will build the linked list and pass the node to your function.
- The output will be the entire list after calling your function.

## Solution

To delete a node in a singly-linked list when only access to that node is given, we can copy the value of the next node to the given node and then delete the next node.

Here's how we can approach this problem:

1. Copy the value of the next node to the given node.
2. Update the `next` pointer of the given node to point to the node after the next node.
3. The next node is effectively removed from the list.

By using this method, we can delete the node without needing access to the head of the linked list.

## Usage

To use the solution, create an instance of the `Solution` class and call the `deleteNode` method with the input parameter `node`:

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

# Example Usage
# Assuming we have a linked list and a reference to the node to be deleted:
# linked list: 4 -> 5 -> 1 -> 9
# node to delete: node with value 5

node_to_delete = ListNode(5)
solution = Solution()
solution.deleteNode(node_to_delete)
```

```python
# Example linked list before deletion: 4 -> 5 -> 1 -> 9
# After deletion: 4 -> 1 -> 9
```

[Link to detailed explanation on Geeksforgeeks](https://www.geeksforgeeks.org/data-structures/linked-list/)


[Link to detailed explanation on Medium](https://karlmatthes.medium.com/abstract-data-types-starting-with-nodes-and-linked-lists-6e7975aa776f)


[Link to detailed explanation on Medium](https://towardsdatascience.com/linked-list-implementation-guide-16ed67be18e4)


[Link to detailed explanation on Geeksforgeeks](https://www.geeksforgeeks.org/delete-a-node-from-linked-list-without-head-pointer/)


## Check Out this video

[![Video Explanation](https://img.youtube.com/vi/Cg0VR2Io1Rk/mqdefault.jpg)](https://youtu.be/Cg0VR2Io1Rk)


[![Video Explanation](https://img.youtube.com/vi/ruat4x3OwQc/mqdefault.jpg)](https://youtu.be/ruat4x3OwQc)


[![Video Explanation](https://img.youtube.com/vi/bJPmNKMtjdk/mqdefault.jpg)](https://youtu.be/bJPmNKMtjdk)


## Complexity Analysis

- **Time Complexity:** O(1). We only perform a constant number of operations to delete the node.
- **Space Complexity:** O(1). We use only constant extra space for the operation.