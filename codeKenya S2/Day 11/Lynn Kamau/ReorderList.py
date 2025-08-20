#Reorder List Leetcode Challenge
#Reorder a linked list in-place such that the nodes are rearranged in a specific order.
#The order is such that the first node is followed by the last node, then the second node, followed by the second last node, and so on.
#This is done without using extra space for another list.
#The algorithm involves finding the middle of the list, reversing the second half, and then merging the two halves.

def reorder_list(head):
    if not head or not head.next:
        return
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    prev, curr = None, slow.next
    slow.next = None
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    first, second = head, prev
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_list(values):
    dummy = ListNode()
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

def print_list(head):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    print(vals)

#Test cases
head = build_list([2,4,6,8])
reorder_list(head)
print_list(head)

head = build_list([2,4,6,8,10])
reorder_list(head)
print_list(head)

# Time Complexity: O(n)
# Space Complexity: O(1)
