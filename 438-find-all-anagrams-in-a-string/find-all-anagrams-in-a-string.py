from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        baseFreq = Counter(p)  
        freq = {}
        ans = []
        l = 0
        for i in range(len(s)):
            freq[s[i]] = freq.get(s[i],0) + 1
            if i - l >= len(p):
                freq[s[l]] -= 1
                if freq[s[l]] == 0:
                    del freq[s[l]]
                l += 1
            if freq == baseFreq:
                ans.append(l)
        return ans
