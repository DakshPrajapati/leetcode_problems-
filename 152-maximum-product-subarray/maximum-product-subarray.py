
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        pos, neg = 1, 1
        ans = -float('inf')

        for i in range(len(nums)):
            pos *= nums[i]
            neg *= nums[i]
            ans = max(ans, pos, neg)
            if pos < 0 and neg > 0:
                pos, neg = neg, pos
            elif pos < 0 and neg < 0:
                pos = 1           
            if pos == 0: pos = 1 
            if neg == 0: neg = 1
        
        return ans
