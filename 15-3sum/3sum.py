class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        answer = set()

        for i in range(0, len(nums)-2):

            if i > 0 and nums[i] == nums[i-1]:
                continue

            start = i + 1
            end = len(nums) - 1
            while start < end:
                total = nums[i] + nums[start] + nums[end]
                if total == 0:
                    answer.add((nums[i], nums[start], nums[end]))
                if total > 0: 
                    end -= 1
                else:
                    start += 1
                
        return (list(answer))
        