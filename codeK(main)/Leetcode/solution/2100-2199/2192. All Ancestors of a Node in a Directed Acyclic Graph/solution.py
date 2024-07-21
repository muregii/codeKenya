class Solution(object):
    def getAncestors(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[List[int]]
        """
        from collections import defaultdict, deque
        
        # Step 1: Create adjacency list for the reversed graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[v].append(u)
        
        # Step 2: Initialize the result list
        ancestors = [set() for _ in range(n)]
        
        # Step 3: Perform DFS to find all ancestors for each node
        def dfs(node, start):
            for parent in graph[node]:
                if parent not in ancestors[start]:
                    ancestors[start].add(parent)
                    dfs(parent, start)
        
        for i in range(n):
            dfs(i, i)
        
        # Step 4: Convert sets to sorted lists
        return [sorted(list(ancestor_set)) for ancestor_set in ancestors]