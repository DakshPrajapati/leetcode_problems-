class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        cities = {}

        for i in range(len(isConnected)):
            neighbours = []
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1:
                    neighbours.append(j)
            cities[i] = neighbours
    
        ans = 0
        seen = []

        def dfs(root):
            if root in seen:
                return 
            seen.append(root)
            candidates = cities[root]
            for c in candidates:
                dfs(c)

        for start in cities:
            if start not in seen:
                ans += 1
                dfs(start)

        return ans
