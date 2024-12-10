class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        for c in s:
            if c in seen:
                seen[c] += 1
            else:
                seen[c] = 1
        for c in t:
            if c in seen:
                seen[c] -= 1
            else:
                return False
        if all(value == 0 for value in seen.values()):
            return True
        return False