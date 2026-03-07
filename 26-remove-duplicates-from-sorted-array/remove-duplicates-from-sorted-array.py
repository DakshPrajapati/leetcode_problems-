class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, right = 1, 1
        while right < len(nums):
            if nums[right] == nums[left-1]:
                right += 1
            elif nums[left-1] != nums[right]:
                nums[left] = nums[right]
                left += 1
                right += 1

        return left