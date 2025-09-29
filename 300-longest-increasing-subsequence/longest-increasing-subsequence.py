class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        longest = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i-1,-1,-1):
                if nums[j] < nums[i]:
                    longest[i] = max(longest[j]+1, longest[i])
        return max(longest)