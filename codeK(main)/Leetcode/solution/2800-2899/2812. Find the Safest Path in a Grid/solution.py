class Solution(object):
    def maximumSafenessFactor(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        # Initialize a 2D list to store the safeness factor of each cell
        safeness = [[0] * n for _ in range(n)]
        
        # Function to calculate the Manhattan distance to the nearest thief
        def manhattan_distance_to_thief(r, c):
            distance = float('inf')
            for x in range(n):
                for y in range(n):
                    if grid[x][y] == 1:
                        distance = min(distance, abs(r - x) + abs(c - y))
            return distance
        
        # Calculate the safeness factor for each cell
        for r in range(n):
            for c in range(n):
                safeness[r][c] = manhattan_distance_to_thief(r, c)
        
        # Dynamic programming to find the path with the maximum safeness factor
        for r in range(1, n):
            safeness[r][0] = min(safeness[r][0], safeness[r-1][0])
        for c in range(1, n):
            safeness[0][c] = min(safeness[0][c], safeness[0][c-1])
        
        for r in range(1, n):
            for c in range(1, n):
                safeness[r][c] = min(safeness[r][c], max(safeness[r-1][c], safeness[r][c-1]))
        
        # The maximum safeness factor is the value at the bottom-right cell
        return safeness[n-1][n-1]