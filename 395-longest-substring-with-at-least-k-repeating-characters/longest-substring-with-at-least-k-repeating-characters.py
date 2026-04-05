class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        
        freq = Counter(s)

        for char,freq in freq.items():
            if freq < k:
                maxLen = 0
                for substring in s.split(char):
                    if substring:
                        maxLen = max(maxLen, self.longestSubstring(substring, k))
                return maxLen

        return len(s)