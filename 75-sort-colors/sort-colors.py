class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start, middle, end = 0, 0, len(nums) - 1
        while middle <= end:
            if nums[middle] == 0:
                nums[middle], nums[start] = nums[start], nums[middle]
                middle += 1
                start += 1
            elif nums[middle] == 1:
                middle += 1
            else:
                nums[middle], nums[end] = nums[end], nums[middle]
                end -= 1
            