class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)

        seen = set()
        stack = set()
        

        def dfs(node: int) -> bool:
            
            if node in stack:
                return False
            if node in seen:
                return True
            stack.add(node)
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            stack.remove(node)
            seen.add(node)
            return True

        result = []
        for i in range(n):
            if dfs(i):
                result.append(i)

        return result