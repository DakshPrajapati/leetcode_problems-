class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort(key = lambda x: (-len(x),x))

        def is_subsequence(word):
            i = 0
            for ch in s:
                if i < len(word) and word[i] == ch:
                    i += 1
                    if i == len(word):
                        return True
            return False
        
        for w in dictionary:
            if is_subsequence(w):
                return w
        return ""