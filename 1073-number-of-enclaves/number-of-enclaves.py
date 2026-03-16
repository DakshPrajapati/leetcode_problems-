class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        dirs =[[0,1], [1,0], [0,-1], [-1,0]]
        
        def dfs(x, y):
            if grid[x][y] == 0:
                return 
            
            grid[x][y] = 0

            for dx, dy in dirs:
                xx = x + dx
                yy = y + dy

                if 0 <= xx < rows and 0 <= yy < cols and grid[xx][yy] == 1:
                    dfs(xx, yy)
        
        for i in range(cols):
            if grid[0][i] == 1:
                dfs(0, i)
            if grid[rows-1][i] == 1:
                dfs(rows-1, i)
        
        for i in range(rows):
            if grid[i][0] == 1:
                dfs(i, 0)
            if grid[i][cols-1] == 1:
                dfs(i, cols-1)
        
        total = sum(sum(row) for row in grid)
        return total
                    

