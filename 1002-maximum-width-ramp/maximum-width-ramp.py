class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        n = len(nums) 

        for idx, num in enumerate(nums):
            if stack and nums[stack[-1]] <= num:
                continue
            else:
                stack.append(idx)
        
        maxDist = 0
        for i in range(n-1,-1,-1):
            while stack and nums[stack[-1]] <= nums[i] and stack[-1] <= i:
                x = stack.pop()
                dist = i - x
                maxDist = max(maxDist, dist)
            
        return maxDist
