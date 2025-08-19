#Reorder List Leetcode Challenge
#Reorder a linked list in-place such that the nodes are rearranged in a specific order.
#The order is such that the first node is followed by the last node, then the second node, followed by the second last node, and so on.
#This is done without using extra space for another list.
#The algorithm involves finding the middle of the list, reversing the second half, and then merging the two halves.

# Recursive approach to reorder a linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next:
            return

        self.left = head

        def dfs(right):
            if not right:
                return
            dfs(right.next)

            if not self.left or self.left == right or self.left.next == right:
                if self.left and (self.left == right or self.left.next == right):
                    right.next = None  
                self.left = None
                return

            temp = self.left.next
            self.left.next = right
            right.next = temp

            self.left = temp

        dfs(head)

def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


# Example usage
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
solution = Solution()
solution.reorderList(head)
print_list(head)  #1 -> 5 -> 2 -> 4 -> 3 -> None


#Time Complexity: O(n) where n is the number of nodes in the linked list
#Space Complexity: O(n)