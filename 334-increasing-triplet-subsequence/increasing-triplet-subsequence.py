class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        smallestFromLeft = [float('inf')]
        largestFromRight = [-float('inf')]

        for i in range(1,len(nums)):
            x = min(smallestFromLeft[-1], nums[i-1])
            smallestFromLeft.append(x)

        a = nums[::-1]
        for i in range(1,len(a)):
            x = max(largestFromRight[-1], a[i-1])
            largestFromRight.append(x)
        
        largestFromRight = largestFromRight[::-1]

        for i in range(len(nums)):
            if smallestFromLeft[i] < nums[i] and nums[i]<largestFromRight[i]:
                return True
            
        return False



