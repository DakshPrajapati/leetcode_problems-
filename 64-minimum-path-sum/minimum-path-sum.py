class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        for i in range(ROWS):
            for j in range(COLS):
                if i == 0 and j - 1 >= 0:
                    grid[i][j] += grid[i][j-1] 
                elif j == 0 and i - 1 >= 0:
                    grid[i][j] += grid[i-1][j]
                elif i > 0 and j > 0:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]