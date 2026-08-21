class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)
        partitionCache = {}
        palindromeCache = {}

        def isPalindrome(left: int, right: int) -> bool:
            if left >= right:
                return True

            if (left, right) in palindromeCache:
                return palindromeCache[(left, right)]

            palindromeCache[(left, right)] = (
                s[left] == s[right]
                and isPalindrome(left + 1, right - 1)
            )

            return palindromeCache[(left, right)]

        def dfs(idx: int, remaining: int) -> bool:
            if idx == n:
                return remaining == 0

            if remaining == 0:
                return False

            # We need at least one character for each remaining partition.
            if n - idx < remaining:
                return False

            if (idx, remaining) in partitionCache:
                return partitionCache[(idx, remaining)]

            for end in range(idx, n):
                if isPalindrome(idx, end):
                    if dfs(end + 1, remaining - 1):
                        partitionCache[(idx, remaining)] = True
                        return True

            partitionCache[(idx, remaining)] = False
            return False

        return dfs(0, 3)