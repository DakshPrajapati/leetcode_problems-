class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        for i in range(len(nums)):
            if nums[i] in count:
                count[nums[i]] = count[nums[i]] + 1
            else:
                count[nums[i]] = 1
        ans = []
        for val, cnt in count.items():
            if cnt > (len(nums)//3):
               ans.append(val)
        return ans
         