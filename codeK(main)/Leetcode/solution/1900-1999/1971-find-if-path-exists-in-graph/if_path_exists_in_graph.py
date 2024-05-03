from collections import defaultdict

class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        if source == destination:
            return True

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        queue = [source]
        visited = set()
        visited.add(source)

        while queue:
            u = queue.pop(0)
            if u == destination:
                return True

            for v in graph[u]:
                if v not in visited:
                    visited.add(v)
                    queue.append(v)

        return False