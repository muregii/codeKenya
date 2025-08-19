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
        return helper(next_node, current)  # tail recursion

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

def print_linked_list(head):
    vals = []
    while head:
        vals.append(str(head.val))
        head = head.next
    print(" → ".join(vals) + " → None")

# Example usage
list_data = [1, 2, 3, 4, 5]
head = build_linked_list(list_data)

print("Original list:")
print_linked_list(head)

reversed_head = reverse_list(head)

print("Reversed list:")
print_linked_list(reversed_head)

# O(n) time 
# O(1) space