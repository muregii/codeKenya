from fractions import Fraction

class Solution(object):
    def mincostToHireWorkers(self, quality, wage, k):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type k: int
        :rtype: float
        """
        # Sort the workers by their wage/quality ratio
        workers = sorted((Fraction(w,q), q, w) for q, w in zip(quality, wage))
        # Initialize a heap and variables to store the total quality and result
        heap = []
        sumq = 0
        res = float('inf')
        
        for ratio, q, w in workers:
            # Add the current worker's quality to the heap
            heapq.heappush(heap, -q)
            sumq += q
            
            # If we have more than k workers, remove the one with the highest quality
            if len(heap) > k:
                sumq += heapq.heappop(heap)
            
            # If we have exactly k workers, calculate the cost
            if len(heap) == k:
                res = min(res, ratio * sumq)
        
        # Convert the result to a float and round it to 5 decimal places
        return float(round(res, 5))