#Linked List Cycle Leetcode Problem
#Given head, the head of a linked list, determine if the linked list has a cycle in it.
#There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
#Internally, pos is used to denote the index of the node that tail's next pointer is connected to. 
#Note that pos is not passed as a parameter.
#Return true if there is a cycle in the linked list. Otherwise, return false.

#Code Optimised for best performance using Floyd's Cycle Detection Algorithm (Tortoise and Hare algorithm)
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def has_cycle(head):
    if not head or not head.next:
        return False

    slow, fast = head, head.next

    while slow != fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next

    return True


# EXAMPLE USAGE
a = ListNode(3)
b = ListNode(2)
c = ListNode(0)
d = ListNode(-4)

a.next = b
b.next = c
c.next = d
d.next = b   # cycle

print(has_cycle(a))  # ✅ True

d.next = None        # no cycle
print(has_cycle(a))  # ✅ False

# Time: O(n)
# Space: O(1) (constant extra memory)
