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

#Test cases to validate the solution
def build_list(values, pos):
    if not values:
        return None
    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i+1]
    if pos != -1:
        nodes[-1].next = nodes[pos] 
    return nodes[0]

head1 = build_list([1,2,3,4], 1)
print("Input: head = [1,2,3,4], index = 1")
print("Output:", has_cycle(head1)) 

head2 = build_list([1,2], -1)
print("Input: head = [1,2], index = -1")
print("Output:", has_cycle(head2))  
 
#Time Complexity: O(n)
#Space Complexity: O(1)
