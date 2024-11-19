class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lenn = min(len(s) for s in strs)
        booll = True
        maxLen = 0
        for i in range(lenn):
            valToCompare = strs[0][i]
            for k in range(len(strs)):
                if strs[k][i] != valToCompare:
                    booll = False
                    return strs[0][0:maxLen]
            maxLen += 1          
        if booll:
            return strs[0][0:maxLen]
        else:
            return ""