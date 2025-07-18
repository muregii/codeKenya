#Assignment 5: 141. Linked List Cycle
#Given head, the head of a linked list, determine if the linked list has a cycle in it.
#There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
#Internally, pos is used to denote the index of the node that tail's next pointer is connected to. 
#Note that pos is not passed as a parameter.
#Return true if there is a cycle in the linked list. Otherwise, return false.

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def has_cycle(head):
    visited = []

    current = head
    while current:
        if current in visited:
            return True 
        visited.append(current)
        current = current.next

    return False

# EXAMPLE USAGE
a = ListNode(3)
b = ListNode(2)
c = ListNode(0)
d = ListNode(-4)

a.next = b
b.next = c
c.next = d
d.next = b

print(has_cycle(a))  

d.next = None
print(has_cycle(a)) 

