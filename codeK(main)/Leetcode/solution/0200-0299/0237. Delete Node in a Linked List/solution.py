# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # If the node is the last node, there's nothing to do
        if node.next is None:
            return

        # Copy the value and next pointer of the next node
        next_node = node.next
        node.val = next_node.val
        node.next = next_node.next

        # The next node is now redundant, so we don't need to do anything with it