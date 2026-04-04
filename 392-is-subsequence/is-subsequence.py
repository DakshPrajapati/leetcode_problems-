class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i1, i2 = 0, 0
        lenS, lenT = len(s), len(t)

        while i1 < len(s) and i2 < len(t):
            if s[i1] == t[i2]:
                i1 += 1
            i2 += 1

        return True if i1 == len(s) else False