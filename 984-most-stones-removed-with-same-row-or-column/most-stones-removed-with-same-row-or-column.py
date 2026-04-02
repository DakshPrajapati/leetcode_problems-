from typing import List

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = {}
        rank = {}

        def find(x):
            if x not in parent:
                parent[x] = x
                rank[x] = 0
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)

            if rootX == rootY:
                return

            if rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            elif rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            else:
                parent[rootY] = rootX
                rank[rootX] += 1

        # Union rows and columns
        for x, y in stones:
            union(x, ~y)   # ~y avoids collision with x

        # Count unique components
        roots = set()
        for x, y in stones:
            roots.add(find(x))

        return len(stones) - len(roots)