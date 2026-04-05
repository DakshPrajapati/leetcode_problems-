class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
     
        if Counter(s) != Counter(goal):
            return False
        
        if s == goal:
            t = set(s)
            return len(t) < len(goal)
        
        if len(s) != len(goal):
            return False

        swap = 0
        for i in range(len(s)):
            if s[i] != goal[i]:
                swap += 1

        if swap == 2:
            return True
        return False