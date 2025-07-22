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
        prev = None
        curr = head

        while curr:
            next_node = curr.next  # Save next node
            curr.next = prev       # Reverse pointer
            prev = curr            # Move prev forward
            curr = next_node       # Move curr forward

        return prev  # New head of reversed list
