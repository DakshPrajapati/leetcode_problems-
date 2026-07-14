class Solution:
    def frequencySort(self, s: str) -> str:
        mapp = defaultdict(int)
        heap = []
        
        for ch in s:
            mapp[ch] += 1
        for k, val in mapp.items():
            heapq.heappush(heap, (-val, k))
        ans = ''
        while heap:
            times, ch = heapq.heappop(heap)
            for i in range(-times):
                ans = ans + ch
        return ans