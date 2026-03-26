class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        minStart, maxEnd = float('inf'), -float('inf')
        
        for trip in trips:
            noOfPass, start, end = trip
            minStart = min(minStart, start)
            maxEnd = max(maxEnd, end)
        
        trips.sort(key = lambda x: x[1])
        heap = []
        t = 0

        i = minStart
        while i < maxEnd:
            if heap and i == heap[0][0]:
                y, x = heapq.heappop(heap)
                capacity += x[0]
                continue
            if trips[t][1] == i:
                heapq.heappush(heap, [trips[t][2],trips[t]])
                capacity -= trips[t][0]
                t += 1
            else: i += 1
            if capacity < 0:
                return False
            if t == len(trips):
                return True
        return False
        
