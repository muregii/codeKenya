from typing import Optional
"""
        To reverse a singly linked list in-place, we iterate through the list while changing the 
        direction of each node’s next pointer. We keep track of:
        - prev: the previous node (initially None)
        - curr: the current node (initially head)
        - next_node: stores the next node before we change curr.next
        
        This results in a reversed list with O(n) time and O(1) space complexity.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
      
        prev = None
        curr = head

        while curr:
            next_node = curr.next  # Store next
            curr.next = prev       # Reverse pointer
            prev = curr            # Move prev forward
            curr = next_node       # Move curr forward

        return prev  # New head of the reversed list


node3 = ListNode(3)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)
head = ListNode(0, node1)

solution = Solution()
node3 = ListNode(3)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)
head = ListNode(0, node1)

solution = Solution()
new_head = solution.reverseList(head)


while new_head:
    print(new_head.val, end=" -> ")
    new_head = new_head.next



new_head = solution.reverseList(head)


while new_head:
    print(new_head.val, end=" -> ")
    new_head = new_head.next


