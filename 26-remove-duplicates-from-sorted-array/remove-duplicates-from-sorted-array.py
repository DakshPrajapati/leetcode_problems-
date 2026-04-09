class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''

        hashmap = {

        }

        0,1,2,3,1,2,2,3,3,4
          i 
          j  
        valJ = 0   
        we insert at j 
        '''
        
        valJ = -101
        i, j = 0, 0

        for i in range(len(nums)):
            if nums[i] != valJ:
                nums[j] = nums[i]
                valJ = nums[j]
                j += 1
        
        return j