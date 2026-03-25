class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-s for s in stones]
        heapq.heapify(h)
        while len(h) > 1 and h[0] != 0:
            s1 = heapq.heappop(h)
            s2 = heapq.heappop(h)
            heapq.heappush(h, s1 - s2)
        return -h[0]