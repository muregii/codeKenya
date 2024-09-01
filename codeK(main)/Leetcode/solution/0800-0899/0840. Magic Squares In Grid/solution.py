class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def isMagic(r, c):
            s = set()
            for i in range(3):
                for j in range(3):
                    if grid[r+i][c+j] < 1 or grid[r+i][c+j] > 9:
                        return False
                    s.add(grid[r+i][c+j])
            if len(s) < 9:
                return False
            if sum(grid[r][c:c+3]) != 15:
                return False
            if sum(grid[r+1][c:c+3]) != 15:
                return False
            if sum(grid[r+2][c:c+3]) != 15:
                return False
            if grid[r][c] + grid[r+1][c] + grid[r+2][c] != 15:
                return False
            if grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1] != 15:
                return False
            if grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2] != 15:
                return False
            if grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != 15:
                return False
            if grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != 15:
                return False
            return True

        count = 0
        for i in range(len(grid) - 2):
            for j in range(len(grid[0]) - 2):
                if isMagic(i, j):
                    count += 1
        return count