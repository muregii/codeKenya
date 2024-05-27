from heapq import heappush, heappop

class Solution(object):
    def kthSmallestPrimeFraction(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(arr)
        # Create a min heap to store the fractions with their indices
        heap = []
        # Initialize the heap with the first element from each row
        for i in range(n - 1):
            heappush(heap, (arr[i] / float(arr[-1]), i, n - 1))
        
        # Extract the smallest fraction k-1 times
        for _ in range(k - 1):
            _, i, j = heappop(heap)
            if j - 1 > i:
                # Push the next fraction from the same row into the heap
                heappush(heap, (arr[i] / float(arr[j - 1]), i, j - 1))
        
        # The kth smallest fraction is at the top of the min heap
        val, i, j = heap[0]
        return [arr[i], arr[j]]