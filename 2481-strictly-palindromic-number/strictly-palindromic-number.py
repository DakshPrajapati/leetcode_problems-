class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:

        def isPalindrome(s: str):
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        for i in range(2, n-1):
            num = ''
            baseNum = n
            while baseNum > 0:
                x = baseNum % i
                num = str(x) + num
                baseNum = baseNum // i
            if not isPalindrome(num):
                return False
        return True    