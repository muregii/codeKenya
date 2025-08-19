# Reversed Lists Leetcode Challenge
# Given the head of a singly linked list, reverse the list, and return the reversed list

#Recursive approach to reverse a linked list
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

def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
reversed_head = reverseList(head)
print_list(reversed_head)  # Output: 5 -> 4 -> 3 -> 2 -> 1 -> None

#Time Complexity: O(n) where n is the number of nodes in the linked list
#Space Complexity: O(n) due to the recursion stack