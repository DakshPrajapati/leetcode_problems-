class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        time = 0
        dirs = [(-1,0), (0, -1), (1, 0), (0, 1)]

        while q and fresh > 0:
            time += 1
            for i in range(len(q)):
                x, y = q.popleft()
                for dx, dy in dirs:
                    xx, yy = x + dx, y + dy
                    if 0 <= xx < rows and 0 <= yy < cols and grid[xx][yy] == 1:
                        grid[xx][yy] = 2
                        fresh -= 1
                        q.append((xx, yy))

        return time if not fresh else -1                