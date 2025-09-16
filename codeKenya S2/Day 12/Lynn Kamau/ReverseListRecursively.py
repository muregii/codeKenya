# Reversed Lists Leetcode Challenge
# Given the head of a singly linked list, reverse the list, and return the reversed list

# Recursive approach to reverse a linked list
def reverseList(head):
    if not head or not head.next:
        return head
    new_head = reverseList(head.next)
    head.next.next = head
    head.next = None
    return new_head

# Example usage:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next  

def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Test case
head = ListNode(0, ListNode(1, ListNode(2, ListNode(3))))
reversed_head = reverseList(head)
print(linked_list_to_list(reversed_head)) 

head = ListNode()
reversed_head = reverseList(head)
print(linked_list_to_list(reversed_head))   

# Time Complexity: O(n)
# Space Complexity: O(n) (recursion stack)
