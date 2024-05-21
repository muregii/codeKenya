# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNodes(self, head):
        # Reverse the linked list
        prev = None
        current = head
        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
        head = prev

        # Remove nodes that have a greater node to the right
        max_val = float('-inf')
        current = head
        prev = None
        while current:
            if current.val < max_val:
                # Remove current node
                prev.next = current.next
            else:
                # Update max_val and move prev
                max_val = current.val
                prev = current
            current = current.next

        # Reverse the linked list again to restore original order
        prev = None
        current = head
        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
        head = prev

        return head