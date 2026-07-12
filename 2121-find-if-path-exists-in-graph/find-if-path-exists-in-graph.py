class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        parent = list(range(n))
        size = [1] * n

        def find(x) -> int: 
            if parent[x] != x:
                parent[x] = parent[parent[x]]
                return find(parent[x])
            else:
                return x
        
        def union(x, y):
            rootX, rootY = find(x), find(y)

            if rootX == rootY:
                return False
            
            if size[rootX] >= size[rootY]:
                parent[rootY] = rootX
                size[rootX] += size[rootY]
            else:
                parent[rootX] = rootY
                size[rootY] += size[rootX]
            
            return True
        
        for edge in edges:
            x, y = edge
            union(x, y)

        return find(source) == find(destination)       
