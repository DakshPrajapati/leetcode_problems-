
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])

        dist = [[float('inf')] * COLS for _ in range(ROWS)]
        dist[0][0] = 0

        heap = [(0, 0, 0)]  # (effort, r, c)
        DIRS = [(1,0), (-1,0), (0,1), (0,-1)]

        while heap:
            cost, r, c = heapq.heappop(heap)

            if cost > dist[r][c]:
                continue

            # early exit
            if (r, c) == (ROWS - 1, COLS - 1):
                return cost

            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc

                if 0 <= nr < ROWS and 0 <= nc < COLS:
                    effort = abs(heights[nr][nc] - heights[r][c])
                    newCost = max(cost, effort)

                    if newCost < dist[nr][nc]:
                        dist[nr][nc] = newCost
                        heapq.heappush(heap, (newCost, nr, nc))

        return 0  # fallback (shouldn't hit)