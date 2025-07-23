# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head):
        # Handle edge cases
        if not head or not head.next:
            return False
        
        # Initialize two pointers - start them at different positions
        slow = head
        fast = head.next
        
        # Floyd's Cycle Detection Algorithm
        while fast and fast.next:
            if slow == fast:        # They meet = cycle exists
                return True
                
            slow = slow.next        # Move 1 step
            fast = fast.next.next   # Move 2 steps
        
        return False                # No cycle found
