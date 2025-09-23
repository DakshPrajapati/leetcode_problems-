class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        mapp = defaultdict(list)
        for u, v in prerequisites:
            mapp[v].append(u)
        
        seen = []
        stack = []

        def dfs(c):
            if c in stack:
                return False
            if c in seen:
                return True
            
            stack.append(c)
            for nei in mapp[c]:
                if not dfs(nei):
                    return False
            stack.pop()
            seen.append(c)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []
        return (seen[::-1])