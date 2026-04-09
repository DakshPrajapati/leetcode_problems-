class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []


        for n in nums:
            if n > 0:
                pos.append(n)
            else:
                neg.append(n)

        v = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = pos[v]
            else:
                nums[i] = neg[v]
                v+=1

        return nums