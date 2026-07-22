class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        heap = [(grid[0][0], (0, 0))]
        heapq.heapify(heap)

        DIRS = [[1,0], [0,1], [-1,0], [0,-1]]
        ROWS, COLS = len(grid), len(grid[0])

        time = [[float('inf') for _ in range(COLS)] for _ in range(ROWS)]
        time[0][0] = grid[0][0]

        while heap:
            c, pos = heapq.heappop(heap)
            x, y = pos
            for dx, dy in DIRS:
                xx, yy = x + dx, y + dy
                if 0 <= xx < ROWS and 0 <= yy < COLS:
                    newCost = max(0, grid[xx][yy] - c)
                    if c + newCost < time[xx][yy]: 
                        heapq.heappush(heap, (c + newCost, [xx, yy]))
                    time[xx][yy] = min(time[xx][yy], c + newCost)

        return time[-1][-1]