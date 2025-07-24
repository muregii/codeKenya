"""You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
"""

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        if self.next:
            return f"{self.value} -> {self.next!r}"
        else:
            return f"{self.value}"
        
#Build a LinkedList class
#More OOP practice
class LinkedList:

    def __init__(self, values=None):
        self.head = None
        if values:
            for v in values:
                self.append(v)

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def to_list(self):
        vals, curr = [], self.head
        while curr:
            vals.append(curr.value)
            curr = curr.next
        return vals

    def __repr__(self):
        return f"{self.to_list()}"
#Understand  
# 0 -> 1 -> 2   class LinkedList
# (0, next=Node(1)) class Node
# 1 2 4-> None l1
# 0 3 5  l2
#output = dummy -> 0 1 2 3 4 5 <- tail
#1. Time    2. Space
    def mergeTwoLists(self, other: 'LinkedList') -> 'LinkedList':
        dummy = Node(0) #loop invariant
        tail = dummy

        l1 = self.head
        l2 = other.head

        #traverse
        while l1 and l2:
            if l1.value < l2.value: # 0 and 1
                tail.next = Node(l1.value)
                l1 = l1.next #advancing through l1 
            else:
                tail.next = Node(l2.value)
                l2 = l2.next
            tail = tail.next

        while l1:
            tail.next = Node(l1.value)
            l1 = l1.next
            tail = tail.next

        while l2:
            tail.next = Node(l2.value)
            l2 = l2.next
            tail = tail.next
        
        output = LinkedList()
        output.head = dummy.next # loop invariant
        return output


l1 = LinkedList([1, 2, 4])
l2 = LinkedList([0, 3, 5])

print(l1.mergeTwoLists(l2))


#Solution to the question at the top. In place
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

    def __repr__(self):
        if self.next:
            return f"{self.val} -> {self.next}"
        else:
            return f"{self.val}"


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        current.next = list1 if list1 else list2
        return dummy.next
l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))
result = Solution().mergeTwoLists(l1, l2)
print(result)









