class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        '''

        maintain a dist[cadidate] = [inf....inf]

        heap = [()] #dist, node

        '''

        dist = [float('inf')] * (n+1)
        dist[k] = 0

        graph = defaultdict(list)
        for time in times:
            source, dest, t = time
            graph[source].append((dest, t))

        heap = [(0, k)]

        while heap:
            curDist, node = heapq.heappop(heap)
            if curDist > dist[node]:
                continue
            
            for nei, weight in graph.get(node, []):
                newDist = curDist + weight
                if newDist < dist[nei]:
                    dist[nei] = newDist
                    heapq.heappush(heap, (newDist, nei))
                
        maxDist = max(dist[1:])
        return maxDist if maxDist < float('inf') else -1

