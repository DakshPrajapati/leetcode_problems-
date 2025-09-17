class Solution:
    def isValid(self, s: str) -> bool:
        
        op = {
            "}": "{",
            ")": "(",
            "]": "["
        }
        stack = []
        for i in range(len(s)):
            if s[i] not in op:
                stack.append(s[i])
            else:
                if stack and stack[-1] == op[s[i]]:
                    stack.pop()
                else:
                    return False
        return True if not stack else False