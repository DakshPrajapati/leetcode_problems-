class Solution:
    def numSquares(self, n: int) -> int:
        candidates = []
        i = 1
        while True:
            if i * i > n: break
            candidates.append(i*i)
            i += 1
        dp = [i for i in range(n+1)] 
        for i in range(n+1):
            for c in candidates:
                if c > i: break
                dp[i] = min(dp[i], 1+dp[i-c])
        return (dp[-1])