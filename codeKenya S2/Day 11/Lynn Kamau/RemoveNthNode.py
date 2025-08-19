# Remove Nth Node from End of List Leetcode Challenge
#Given the head of a linked list, remove the nth node from the end of the list and return its head.
#The algorithm uses two pointers to find the nth node from the end in a single pass.    
#The first pointer advances n+1 steps ahead, and then both pointers move together until the first pointer reaches the end.


def remove_nth_from_end(head, n):
    dummy = ListNode(0, head)
    first = second = dummy
    for _ in range(n + 1):
        first = first.next
    while first:
        first = first.next
        second = second.next
    second.next = second.next.next
    return dummy.next

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

# usage
head = build_list([1,2,3,4,5])
head = remove_nth_from_end(head, 2)
print_list(head)  # Output: [1, 2, 3, 5]

# Time Complexity: O(n)
# Space Complexity: O(1)
