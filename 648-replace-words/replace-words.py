class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        words = sentence.split()
        roots = dictionary
        roots.sort()
        def isDeri(root, word): 
            if len(root) > len(word):
                return False
            n = len(root)
            if root == word[:n]:
                return True

        for idx, word in enumerate(words):
            for root in roots:
                if isDeri(root, word):
                    words[idx] = root
                    break
        
        return ' '.join(words)