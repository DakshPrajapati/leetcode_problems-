class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []
        def dfs():
            if len(sol) == len(nums):
                res.append(sol[:])
                return
            for v in nums:
                if v not in sol:
                    sol.append(v)
                    dfs()
                    sol.pop()
        dfs()
        return (res)