class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        g = [-x for x in gifts]
        heapq.heapify(g)
        while k > 0:
            pile = -heapq.heappop(g)
            heapq.heappush(g, -math.isqrt(pile))
            k -= 1
        return -(sum(g))