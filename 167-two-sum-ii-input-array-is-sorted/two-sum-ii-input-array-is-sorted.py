class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = len(nums) - 1
        while start < end:
            total = nums[start] + nums[end]
            if total == target: return [start+1, end+1]
            if total < target: start += 1
            else: end -= 1
        
