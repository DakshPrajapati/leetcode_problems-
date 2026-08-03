class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)

        def returnDays(wei: int) -> int:
            days = 1
            curWeights = 0
            for i in range(len(weights)):
                if curWeights + weights[i] > wei:
                    days += 1
                    curWeights = weights[i]
                else:
                    curWeights += weights[i]
            return days
        
        ans = r
        while l <= r:
            m = (r + l) // 2
            d = returnDays(m)
            if d <= days:
                r = m - 1
                ans = m
            else:
                l = m + 1
        
        return (ans)