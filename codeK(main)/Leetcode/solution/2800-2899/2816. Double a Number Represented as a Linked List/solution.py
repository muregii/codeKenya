# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def doubleIt(self, head):
        # Helper function to convert linked list to integer
        def listToInt(node):
            num = 0
            while node:
                num = num * 10 + node.val
                node = node.next
            return num
        
        # Helper function to convert integer to linked list
        def intToList(num):
            # If the number is 0, return a list node with value 0
            if num == 0:
                return ListNode(0)
            # Initialize the previous node to None
            prev = None
            while num > 0:
                # Get the last digit
                digit = num % 10
                # Create a new node with the digit
                current = ListNode(digit)
                # Set the next of the current node to the previous node
                current.next = prev
                # Update the previous node to be the current node
                prev = current
                # Remove the last digit from the number
                num //= 10
            return prev
        
        # Convert the linked list to an integer
        num = listToInt(head)
        # Double the integer
        doubled_num = num * 2
        # Convert the doubled integer back to a linked list
        return intToList(doubled_num)

# Example usage:
# Assuming we have a linked list 1 -> 8 -> 9 representing the number 189
# After calling doubleIt, we should get a linked list 3 -> 7 -> 8 representing the number 378