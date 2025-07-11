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
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next         # move 1 step
            fast = fast.next.next    # move 2 steps

            if slow == fast:
                return True  # cycle detected

        return False  # no cycle
