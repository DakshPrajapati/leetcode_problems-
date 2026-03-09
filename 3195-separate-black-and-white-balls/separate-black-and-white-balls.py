class Solution:
    def minimumSteps(self, s1: str) -> int:
        w, b = 0, 0
        count = 0
        s = list(s1)
        while w < len(s) and b < len(s):
            if s[w] == '0' and s[b] == '1':
                s[w], s[b] = s[b], s[w]
                b += 1
                count += abs(w-b+1)
            elif s[w] == '1':
                w += 1
            elif s[b] == '0':
                b += 1
                w += 1
        return count