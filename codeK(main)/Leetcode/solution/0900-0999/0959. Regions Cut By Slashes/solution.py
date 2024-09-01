class Solution(object):
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        n = len(grid)
        # Initialize Union-Find data structure
        parent = list(range(4 * n * n))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootX] = rootY

        for r in range(n):
            for c in range(n):
                root = 4 * (r * n + c)
                val = grid[r][c]
                # Union the parts of the square itself
                if val in "/ ":
                    union(root + 0, root + 3)
                    union(root + 1, root + 2)
                if val in "\\ ":
                    union(root + 0, root + 1)
                    union(root + 2, root + 3)
                
                # Union with the right cell
                if c + 1 < n:
                    union(root + 1, 4 * (r * n + (c + 1)) + 3)
                # Union with the bottom cell
                if r + 1 < n:
                    union(root + 2, 4 * ((r + 1) * n + c) + 0)
        
        # Count the number of distinct regions
        return sum(find(x) == x for x in range(4 * n * n))