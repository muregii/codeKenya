# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        #find the mid of the list using f & s ptrs
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_half = self.reverseList(slow)

        first_half, second_half_copy = head, second_half
        while second_half:
            if first_half.val != second_half.val:
                return False
            first_half = first_half.next
            second_half = second_half.next

        self.reverseList(second_half_copy)
        
        return True
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
