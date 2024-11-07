class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = []
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] not in seen:
                seen.append(nums[i])
                i+=1
            else:
                nums.pop(i)
                n-=1