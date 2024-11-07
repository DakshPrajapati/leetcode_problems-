class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        maxx = 0
        cnt = 0
        for i in range(n):
            if nums[i] == 0:
                cnt = 0
            else:
                cnt += 1
                maxx = max(maxx,cnt)
        return maxx