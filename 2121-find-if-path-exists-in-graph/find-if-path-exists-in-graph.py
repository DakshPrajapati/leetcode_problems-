class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        parent = list(range(n))
        size = [1] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)

            if rootX == rootY:
                return False
            
            if size[rootX] < size[rootY]:
                rootX, rootY = rootY, rootX

            parent[rootY] = rootX
            size[rootX] += size[rootY]

            return True
        
        for edge in edges:
            x, y = edge
            union(x, y)
        
        return find(source) == find(destination)