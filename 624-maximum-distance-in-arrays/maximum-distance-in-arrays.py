class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        minNum = arrays[0][0]
        maxNum = arrays[0][-1]
        maxDist = 0

        for i in range(1, len(arrays)):
            currentMin = arrays[i][0]
            currentMax = arrays[i][-1]

            maxDist = max(
                maxDist,
                abs(currentMax - minNum),
                abs(maxNum - currentMin)
            )

            minNum = min(minNum, currentMin)
            maxNum = max(maxNum, currentMax)

        return maxDist