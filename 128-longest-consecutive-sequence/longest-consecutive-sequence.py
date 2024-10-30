class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        maxcount = 0
        count = 0
        zeros = 0
        nums.sort()
        if n == 0:
            return 0
        if n == 1:
            return 1
        for i in range(1,n):
            if nums[i] == nums[i-1] + 1:
                count += 1
                if count > maxcount:
                    maxcount = count
            elif nums[i] == nums[i-1]:
                count = count
            else:
                count = 0 
        return maxcount + 1 