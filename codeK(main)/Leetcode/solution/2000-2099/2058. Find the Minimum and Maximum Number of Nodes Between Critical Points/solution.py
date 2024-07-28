# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        # List to store positions of critical points
        critical_points = []
        
        # Initialize pointers and position counter
        prev, curr, pos = head, head.next, 1
        
        while curr.next:
            next_node = curr.next
            # Check if current node is a local maxima or minima
            if (curr.val > prev.val and curr.val > next_node.val) or (curr.val < prev.val and curr.val < next_node.val):
                critical_points.append(pos)
            
            # Move to the next set of nodes
            prev = curr
            curr = next_node
            pos += 1
        
        # If there are fewer than 2 critical points, return [-1, -1]
        if len(critical_points) < 2:
            return [-1, -1]
        
        # Calculate min and max distance between critical points
        min_distance = float('inf')
        max_distance = critical_points[-1] - critical_points[0]
        
        for i in range(1, len(critical_points)):
            min_distance = min(min_distance, critical_points[i] - critical_points[i - 1])
        
        return [min_distance, max_distance]