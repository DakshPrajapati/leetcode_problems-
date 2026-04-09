class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = [0]

        for n in nums:
            if n == 0:
                ans.append(0)
            else:
                ans.append(ans[-1] + 1)
        
        return (max(ans))