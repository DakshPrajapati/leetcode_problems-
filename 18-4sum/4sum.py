class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []

        for i in range(0,n):
            if i>0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1,n):
                if j>i+1 and nums[j] == nums[j-1]:
                    continue
                
                left, right = j + 1, n - 1
                while left < right:
                    summ = nums[i] + nums[j] + nums[left] + nums[right]
                    if summ == target:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])          
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif summ < target:
                        left += 1
                    else:
                        right -= 1
        return ans