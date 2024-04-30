from collections import defaultdict

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        if n == 1:
            return [0]

        # Create an adjacency list to represent the tree
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Find all leaf nodes
        leaves = [node for node in range(n) if len(graph[node]) == 1]

        # Trim the tree layer by layer until we reach the center
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves

        return leaves