class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = 0
        ones = 0
        twos = 0
        for i in range(0,len(nums)):
            if nums[i] == 0:
                zeros = zeros + 1
            elif nums[i] == 1:
                ones = ones + 1
            elif nums[i] == 2:
                twos = twos + 1
        nums.clear()
        for i in range(0,zeros):
            nums.append(0)
        for i in range(0,ones):
            nums.append(1)
        for i in range(0, twos):
            nums.append(2)
