class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        '''

            [0,0,1,1,0,1,0,0,1,0],
            [1,1,0,1,1,0,1,1,1,0],
            [1,0,1,1,1,0,0,1,1,0],
            [0,1,1,0,0,0,0,1,0,1],
            [0,0,0,0,0,0,1,1,1,0],
            [0,1,0,1,0,1,0,1,1,1],
            [1,0,1,0,1,1,0,0,0,1],
            [1,1,1,1,1,1,0,0,0,0],
            [1,1,1,0,0,1,0,1,0,1],
            [1,1,1,0,1,1,0,1,1,0]]

        '''
        DIRS = [(0,1), (1,0), (-1,0), (0,-1)]

        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            grid[r][c] = 1
            isClosed = True

            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc

                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS:
                    isClosed = False
                elif grid[nr][nc] == 0:
                    isClosed = dfs(nr, nc) and isClosed

            return isClosed


        count = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    if dfs(r, c):
                        count += 1

        return count