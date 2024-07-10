import heapq

class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """
        # Create a list of projects with their capital and profit
        projects = list(zip(capital, profits))
        
        # Min-heap for projects based on capital required
        min_heap = []
        # Max-heap for available projects based on profit
        max_heap = []
        
        # Add all projects to the min-heap
        for c, p in projects:
            heapq.heappush(min_heap, (c, p))
        
        for _ in range(k):
            # Move all feasible projects to the max-heap
            while min_heap and min_heap[0][0] <= w:
                c, p = heapq.heappop(min_heap)
                heapq.heappush(max_heap, -p)  # Use negative to simulate max-heap
            
            # If no projects can be done, break
            if not max_heap:
                break
            
            # Select the project with the maximum profit
            w -= heapq.heappop(max_heap)
        
        return w