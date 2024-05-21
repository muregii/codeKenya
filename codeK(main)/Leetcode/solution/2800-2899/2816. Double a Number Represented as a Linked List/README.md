# Leetcode - Double a Number Represented as a Linked List

## Problem Description

You are given the `head` of a **non-empty** linked list representing a non-negative integer without leading zeroes.

Return *the `head` of the linked list after **doubling** it*.


**Constraints:**

- The number of nodes in the list is in the range `[1, 104]`
- `0 <= Node.val <= 9`
- The input is generated such that the list represents a number that does not have leading zeros, except the number `0` itself.

## Solution

To solve this problem, we need to double the integer represented by the linked list. Since the linked list represents a large integer, we need to handle each digit carefully, taking care of any carry-over that occurs during the doubling process.

Here's how we can approach this problem:

1. Reverse the linked list to simplify the doubling process, starting from the least significant digit.
2. Initialize a variable `carry` to 0.
3. Traverse the reversed list:
   - Double the current node's value and add the carry.
   - Update the node's value to be the new value modulo 10 (to handle the single digit).
   - Update the carry to be the new value divided by 10 (to handle the carry-over to the next digit).
4. If there is any remaining carry after processing all nodes, add a new node with the carry value.
5. Reverse the list again to restore the original order but with the doubled values.
6. Return the head of the modified list.

By reversing the list, we simplify the doubling process by handling it from the least significant digit to the most significant digit, and then we reverse the list back to its original order.

## Usage

To use the solution, create an instance of the `Solution` class and call the `doubleIt` method with the input parameter `head`:

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def doubleIt(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
```

```python
# Example linked list before doubling: 1 -> 2 -> 3
# After doubling: 2 -> 4 -> 6
```

[Link to detailed explanation on Geeksforgeeks](https://www.geeksforgeeks.org/double-a-number-represented-in-a-linked-list/)


[Link to detailed explanation on Medium](https://medium.com/rakulee/2816-double-a-number-represented-as-a-linked-list-e3d2f5f38aee)

## Check Out this video

[![Video Explanation](https://img.youtube.com/vi/KpjU5dy-ZcA/mqdefault.jpg)](https://youtu.be/KpjU5dy-ZcA)


[![Video Explanation](https://img.youtube.com/vi/hqmrMwxbG7c/mqdefault.jpg)](https://youtu.be/hqmrMwxbG7c)

## Complexity Analysis

- **Time Complexity:** O(n), where n is the number of nodes in the linked list. We traverse the list three times (reverse, traverse, and reverse again).
- **Space Complexity:** O(1). We use only constant extra space for pointers and variables.