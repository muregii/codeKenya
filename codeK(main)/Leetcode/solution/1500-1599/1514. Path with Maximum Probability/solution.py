import heapq

class Solution(object):
    def maxProbability(self, n, edges, succProb, start, end):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start: int
        :type end: int
        :rtype: float
        """
        # Create an adjacency list
        graph = {i: [] for i in range(n)}
        for i, (a, b) in enumerate(edges):
            graph[a].append((b, succProb[i]))
            graph[b].append((a, succProb[i]))
        
        # Priority queue for max probability path (Dijkstra-like)
        max_heap = [(-1, start)]  # Use negative probability to simulate max-heap
        probabilities = [0] * n
        probabilities[start] = 1
        
        while max_heap:
            curr_prob, node = heapq.heappop(max_heap)
            curr_prob = -curr_prob
            
            if node == end:
                return curr_prob
            
            for neighbor, prob in graph[node]:
                new_prob = curr_prob * prob
                if new_prob > probabilities[neighbor]:
                    probabilities[neighbor] = new_prob
                    heapq.heappush(max_heap, (-new_prob, neighbor))
        
        return 0