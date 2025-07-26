# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None. Do not return anything, modify head in-place instead.
        """
        self.left = head

        def recurse(right):
            if not right:
                return True

            # Recursively go to the end
            if not recurse(right.next):
                return False

            # Stop when left meets or crosses right
            if self.left == right or self.left.next == right:
                right.next = None
                return False

            # Reorder nodes
            temp = self.left.next
            self.left.next = right
            right.next = temp

            # Move left pointer forward
            self.left = temp
            return True

        recurse(head)
