class Solution:
    def check(self, nums: List[int]) -> bool:
       
        dipIdx = None
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                if not dipIdx:
                    dipIdx = i
                else:
                    return False
            
        if dipIdx == None: return True
    
        return nums[0] >= nums[-1]