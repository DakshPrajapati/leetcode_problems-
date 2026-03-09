class Solution:
    def numRescueBoats(self, nums: List[int], limit: int) -> int:
        nums.sort(reverse=True)
        i, j = 0, len(nums) - 1
        while i <= j:
            if nums[i] + nums[j] <= limit: j -= 1
            i += 1
        return i