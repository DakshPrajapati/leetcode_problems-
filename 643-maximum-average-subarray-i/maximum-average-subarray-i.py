from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        prefix = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            prefix[i + 1] = prefix[i] + nums[i]

        maxSum = float("-inf")

        for i in range(k, len(nums) + 1):
            windowSum = prefix[i] - prefix[i - k]
            maxSum = max(maxSum, windowSum)

        return maxSum / k