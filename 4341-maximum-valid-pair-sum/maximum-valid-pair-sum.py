class Solution:
    def maxValidPairSum(self, nums: list[int], k: int) -> int:
        postMax = []
        lastMax = 0
        n = len(nums)

        for i in range(n-1, -1, -1):
            curMax = max(lastMax, nums[i])
            postMax.append(curMax)
            lastMax = curMax
        
        postMax = postMax[::-1]

        res = 0
        for i in range(n-k):
            res = max(res, nums[i]+postMax[i+k])
        
        return res