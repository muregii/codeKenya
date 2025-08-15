# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Base case: empty list or single node
        if not head or not head.next:
            return head
        
        # Reverse the rest of the list
        new_head = self.reverseList(head.next)

        # Reverse the current node's pointer
        head.next.next = head
        head.next = None

        return new_head
