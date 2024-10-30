class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0 
        j = 0
        maxx = 0
        n = len(s)
        count = 0
        seen = []
        if n == 0: return 0
        elif n == 1 : return 1
        while True:
            if s[j] not in seen:
                seen.append(s[j])
                j += 1
            else:
                seen.pop(0)
                i += 1
            
            if j == n and i < n-1:
                j = n-1
            elif j==n-1 and i ==n-1:
                break

            maxx = max(len(seen), maxx)
        return maxx
            
