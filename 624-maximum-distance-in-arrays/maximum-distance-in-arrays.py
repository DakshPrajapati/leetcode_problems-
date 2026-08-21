class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        curMin = arrays[0][0]
        curMax = arrays[0][-1]
        maxDist = 0

        for i in range(1, len(arrays)):
            localMin = arrays[i][0]
            localMax = arrays[i][-1]

            maxDist = max(maxDist,
                abs(localMax - curMin),
                abs(localMin - curMax)
            )
        
            curMin = min(curMin, localMin)
            curMax = max(curMax, localMax)

        return (maxDist)