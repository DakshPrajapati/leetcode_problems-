class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def isValid(base, lenString, lenS):
            i, j = 0, 0
            baseLen, targetLen = lenString, lenS

            while i < baseLen and j < targetLen:
                if base[i] == s[j]:
                    i += 1
                j += 1
            
            return True if i >= len(base) else False

        def countLex(s):
            base = 256
            res = 0
            for c in s:
                res = res * base + ord(c)
            return res
    
        words = [[len(x), -countLex(x), x] for x in dictionary]
        words.sort(key=lambda x: (x[0], x[1]), reverse=True)
        lenS = len(s)

        for word in words:
            length, lex, w = word
            if isValid(w, length, lenS):
                return w
            
        return ""
        
