# Reversed Lists Leetcode Challenge
# Given the head of a singly linked list, reverse the list, and return the reversed list

class ListNode: 
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    def helper(current, prev=None):
        if not current:
            return prev 
        next_node = current.next
        current.next = prev
        return helper(next_node, current) 
    return helper(head)

def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    return vals

#Test cases to validate the solution
list_data = [0,1,2,3]
head = build_linked_list(list_data)
print("head =", list_data)
reversed_head = reverse_list(head)
print(linked_list_to_list(reversed_head))

list_data = []
head = build_linked_list(list_data)
print("\nhead =", list_data)
reversed_head = reverse_list(head)
print( linked_list_to_list(reversed_head))

# Time Complexity: O(n)
# Space Complexity: O(1) (excluding the output list)