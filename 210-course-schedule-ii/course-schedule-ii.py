class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjMap = defaultdict(list)
        for c, d in prerequisites:
            adjMap[d].append(c)
        
        seen = []
        stack = []

        def dfs(root):
            if root in stack:
                return False
            if root in seen:
                return True

            stack.append(root)
            for nei in adjMap[root]:
                if not dfs(nei):
                    return False
            stack.pop()
            seen.append(root)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []

        return seen[::-1]
        