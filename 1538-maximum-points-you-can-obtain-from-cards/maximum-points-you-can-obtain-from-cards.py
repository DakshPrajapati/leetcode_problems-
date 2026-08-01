from typing import List


class Solution:
    def maxScore(self, nums: List[int], k: int) -> int:
        n = len(nums)

        currentScore = sum(nums[:k])
        maxScore = currentScore

        for rightCount in range(1, k + 1):
            leftIndex = k - rightCount
            rightIndex = n - rightCount

            currentScore -= nums[leftIndex]
            currentScore += nums[rightIndex]

            maxScore = max(maxScore, currentScore)

        return maxScore