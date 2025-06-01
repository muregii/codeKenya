class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next 

from typing import Optional

def hasCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    tortoise = head
    hare = head.next

    while hare and hare.next:
        if tortoise == hare:
            return True
        tortoise = tortoise.next
        hare = hare.next.next
    return False

        

    