# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        current = dummy
        sum = 0
        
        while head:
            if head.val == 0:
                if sum != 0:
                    current.next = ListNode(sum)
                    current = current.next
                    sum = 0
            else:
                sum += head.val
            head = head.next
        
        return dummy.next