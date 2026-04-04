from collections import deque
from typing import List

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        res = list(dominoes)
        
        q = deque()
        
        # Initialize queue with all R and L positions
        for i, c in enumerate(dominoes):
            if c != '.':
                q.append((i, c, 0))  # (index, direction, time)
        
        # Track the earliest force reaching each index
        forces = [None] * n
        
        while q:
            i, direction, time = q.popleft()
            
            if forces[i] is not None:
                # Conflict resolution: if same time, cancel
                prevDir, prevTime = forces[i]
                if prevTime == time and prevDir != direction:
                    forces[i] = ('.', time)
                continue
            
            forces[i] = (direction, time)
            
            if direction == 'R' and i + 1 < n:
                if forces[i + 1] is None:
                    q.append((i + 1, 'R', time + 1))
            
            if direction == 'L' and i - 1 >= 0:
                if forces[i - 1] is None:
                    q.append((i - 1, 'L', time + 1))
        
        # Build result
        result = list(dominoes)
        
        for i in range(n):
            if forces[i] is not None:
                direction, _ = forces[i]
                if direction == '.':
                    result[i] = '.'
                else:
                    result[i] = direction
        
        return "".join(result)