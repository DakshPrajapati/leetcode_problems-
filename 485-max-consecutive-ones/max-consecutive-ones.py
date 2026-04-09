class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
      
        lastMax = 0
        curr = 0
        for n in nums:
            if n == 0:
                curr = 0
            else:
                curr += 1
                lastMax = max(lastMax, curr)
        
        return lastMax