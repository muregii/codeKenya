#Merge Two Sorted Lists Leetcode Challenge
#You are given the heads of two sorted linked lists list1 and list2.
#Merge the two lists in a one sorted list.
#The list should be made by splicing together the nodes of the first two lists.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(list1, list2):
    dummy = ListNode()
    current = dummy

    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    if list1:
        current.next = list1
    if list2:
        current.next = list2

    return dummy.next

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
list1 = build_linked_list([2,4,6,8])
list2 = build_linked_list([1, 3, 5, 7, 9])

merged = merge_two_lists(list1, list2)
print_linked_list(merged)