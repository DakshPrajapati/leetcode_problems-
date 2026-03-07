class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        resLen = 0
        l = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            if r - l + 1 > resLen: resLen = r - l + 1
        return resLen
