class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0]*(len(word1)+1) for _ in range(len(word2)+1)]
        for i in range(len(dp[0])): dp[0][i] = i
        for j in range(len(dp)): dp[j][0] = j
        
        ROWS, COLS = len(dp), len(dp[0])

        for i in range(1, ROWS):
            for j in range(1, COLS):
                if word1[j-1] == word2[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        return (dp[-1][-1])