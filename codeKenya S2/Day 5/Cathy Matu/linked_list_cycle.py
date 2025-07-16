# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head  # Initialize both pointers

        while fast and fast.next:  # Ensure we don't hit None
            slow = slow.next       # Move slow pointer by 1
            fast = fast.next.next  # Move fast pointer by 2

            if slow == fast:
                return True  # Cycle detected

        return False  # No cycle
