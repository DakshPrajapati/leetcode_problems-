class Solution:
    def compress(self, chars: List[str]) -> int:
        l, r = 0, 0
        answerIndex = 0
        while r < len(chars):
            while r < len(chars) and chars[l] == chars[r]:
                r += 1
            chars[answerIndex] = chars[l]
            answerIndex += 1
            if r - l > 1:
                n = str(r - l) 
                for i in range(len(n)):
                    chars[answerIndex] = n[i]
                    answerIndex += 1
            l = r
        return answerIndex