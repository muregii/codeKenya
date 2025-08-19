#Merge Two Sorted Lists Leetcode Challenge
#You are given the heads of two sorted linked lists list1 and list2.
#Merge the two lists in a one sorted list.
#The list should be made by splicing together the nodes of the first two lists.

#Solving the problem Recursively
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(list1, list2):
    if not list1:
        return list2
    if not list2:
        return list1

    if list1.val < list2.val:
        list1.next = merge_two_lists(list1.next, list2)
        return list1
    else:
        list2.next = merge_two_lists(list1, list2.next)
        return list2

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
    current = head
    while current:
        print(current.val, end=" → ")
        current = current.next
    print("None")

# Example usage
list1 = build_linked_list([2, 4, 6, 8])
list2 = build_linked_list([1, 3, 5, 7, 9])

merged = merge_two_lists(list1, list2)
print_linked_list(merged)

#Time Complexity: O(n + m) where n and m are the lengths of the two linked lists.
#Space Complexity: O(n + m) for the recursive stack space.