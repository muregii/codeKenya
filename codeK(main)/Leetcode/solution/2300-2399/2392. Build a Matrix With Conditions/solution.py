class Solution(object):
    def buildMatrix(self, k, rowConditions, colConditions):
        """
        :type k: int
        :type rowConditions: List[List[int]]
        :type colConditions: List[List[int]]
        :rtype: List[List[int]]
        """
        def topological_sort(conditions, k):
            graph = {i: [] for i in range(1, k+1)}
            in_degree = {i: 0 for i in range(1, k+1)}
            for u, v in conditions:
                graph[u].append(v)
                in_degree[v] += 1
            queue = [i for i in range(1, k+1) if in_degree[i] == 0]
            order = []
            while queue:
                node = queue.pop(0)
                order.append(node)
                for neighbor in graph[node]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)
            return order if len(order) == k else []

        row_order = topological_sort(rowConditions, k)
        col_order = topological_sort(colConditions, k)
        
        if not row_order or not col_order:
            return []
        
        row_pos = {num: i for i, num in enumerate(row_order)}
        col_pos = {num: i for i, num in enumerate(col_order)}
        
        matrix = [[0] * k for _ in range(k)]
        for num in range(1, k + 1):
            matrix[row_pos[num]][col_pos[num]] = num
        
        return matrix