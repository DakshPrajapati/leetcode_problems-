class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        size = [1] * (n+1)
        parent = list(range(n+1))

        def find(x: int) -> int:   
            if parent[x] != x:
                parent[x] = parent[parent[x]]
                return find(parent[x])    
            return x
        
        def union(x: int, y: int) -> bool:
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
            if not union(x, y):
                return edge
        