class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0
        visited = set()

        def dfs(r, c):
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                grid[r][c] == '0' or
                    (r, c) in visited):
                return

            visited.add((r, c))

            dfs(r - 1, c)  # explore up
            dfs(r + 1, c)  # explore down
            dfs(r, c - 1)  # explore left
            dfs(r, c + 1)  # explore right

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    dfs(r, c)
                    islands += 1

        return islands
