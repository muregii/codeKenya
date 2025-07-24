# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        fast = slow = dummy
        
        # Moving fast pointer n+1 steps ahead
        for _ in range(n + 1):
            fast = fast.next
        
        # Moving both pointers
        while fast:
            fast = fast.next
            slow = slow.next
        
        # Skipping the nth node from the end
        slow.next = slow.next.next
        
        return dummy.next
