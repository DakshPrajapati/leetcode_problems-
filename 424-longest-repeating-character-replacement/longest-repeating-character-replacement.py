class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        seen = [0] * 26
        lenn, maxLen = 0, 0
        while r < len(s):
            seen[ord(s[r])-ord('A')] += 1
            r += 1
            lenn += 1
            while lenn - max(seen) > k:
                lenn -= 1
                seen[ord(s[l])-ord('A')] -= 1
                l += 1
            maxLen = max(lenn, maxLen)
    
        return maxLen
             