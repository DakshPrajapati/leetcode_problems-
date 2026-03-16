class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)

        state = [0] * n
        # 0 = unvisited
        # 1 = visiting
        # 2 = safe

        def dfs(node: int) -> bool:
            if state[node] != 0:
                return state[node] == 2

            state[node] = 1

            for nei in graph[node]:
                if state[nei] == 1 or not dfs(nei):
                    return False

            state[node] = 2
            return True

        result = []
        for i in range(n):
            if dfs(i):
                result.append(i)

        return result