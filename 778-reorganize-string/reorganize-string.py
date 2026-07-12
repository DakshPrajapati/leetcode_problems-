class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        heap = []

        for key, val in counts.items():
            if val > math.ceil(len(s) / 2):
                return ""
            heapq.heappush(heap, (-val, key))

        ans = "#"
        while heap:
            freq, ch = heapq.heappop(heap)
            if ch != ans[-1]:
                ans = ans + ch
                freq += 1
            else:
                #safty check
                freq2, ch2 = heapq.heappop(heap)
                ans = ans + ch2 
                freq2 += 1
                if freq2 != 0:
                    heapq.heappush(heap, (freq2, ch2))
            if freq != 0:
                heapq.heappush(heap, (freq, ch))
            
        return ans[1:]