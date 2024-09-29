class Solution(object):
    def countSubIslands(self, grid1, grid2):
        """
        :type grid1: List[List[int]]
        :type grid2: List[List[int]]
        :rtype: int
        """
        def dfs(i, j):
            if i < 0 or i >= len(grid2) or j < 0 or j >= len(grid2[0]) or grid2[i][j] == 0:
                return True
            grid2[i][j] = 0
            is_sub_island = grid1[i][j] == 1
            is_sub_island &= dfs(i - 1, j)
            is_sub_island &= dfs(i + 1, j)
            is_sub_island &= dfs(i, j - 1)
            is_sub_island &= dfs(i, j + 1)
            return is_sub_island
        
        count = 0
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] == 1 and dfs(i, j):
                    count += 1
        return count