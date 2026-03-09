class Solution:  # 672 ms, faster than 79.33%
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # Example: [10,1,2,4,7,4,3,1], limit = 5
        dqMax, dqMin = deque(), deque()
        ans = 0
        l = 0
        n = len(nums)
        for r in range(n):
            while dqMax and nums[dqMax[-1]] <= nums[r]:  # If we found a larger element then no need to keep smaller elements
                dqMax.pop()
            while dqMin and nums[dqMin[-1]] >= nums[r]:  # If we found a smaller element then no need to keep larger elements
                dqMin.pop()
            dqMax.append(r)
            dqMin.append(r)
            
            while nums[dqMax[0]] - nums[dqMin[0]] > limit:
                l += 1  # Shrink size by moving the left pointer
                if dqMax[0] < l: dqMax.popleft()
                if dqMin[0] < l: dqMin.popleft()
                    
            ans = max(ans, r - l + 1)
            
        return ans