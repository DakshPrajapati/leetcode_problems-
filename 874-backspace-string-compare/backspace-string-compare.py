class Solution:

    @staticmethod
    def helper(s1: str) -> list:
        stack = []
        for ch in s1:
            if ch == '#' and stack:
                stack.pop()
            elif ch != '#':
                stack.append(ch)
        return stack

    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.helper(s) == self.helper(t)
                        
