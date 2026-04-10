class Solution:
    def decrypt(self, nums: List[int], k: int) -> List[int]:
        '''
        - we slice for i and i + k
        - we start from i and go till k adding 
        - main tain a dynamic window, when r- l + 1 == k, add ans[l]
            loop till left pointer is at the end. 

            we need to handle k > len in seperate 
            
        [ done ]    if k < 0:
                        nums.reveserse()

        [ done ]    summ = sum(x[:k])

        [ done ]    l = 0
                    r = k
            
            while l < len(nums):
                if r - l + 1:
                    ans[l-1] = sum
                    sum -= nums[l]
                    l += 1
                r += 1
                sum += nums[r]
        '''
        nextK = abs(k)
        if k < 0:
            nums = nums[::-1]

        curSum = sum(nums[:nextK])
        l = 0
        r = nextK - 1
        n = len(nums)

        ans = [0] * n

        while l < n:
            if r - l + 1 == nextK:
                ans[l-1] = curSum
                curSum -= nums[l]
                l += 1
            r += 1
            modR = r % n
            curSum += nums[modR]
        
        if k > 0:
            return ans
        else:
            return ans[::-1]


