
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseLinkedList(self, head: ListNode) -> ListNode:
    current = head
    prev = None

    while current:
        temp = current.next
        current.next = prev
        prev = current
        current = temp
    return prev


