class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secretCounts = Counter(secret)
        
        bulls, cows = 0, 0 
        for i in range(len(guess)):
            if secret[i] == guess[i]:
                bulls += 1
                secretCounts[guess[i]] -= 1

        for i in range(len(guess)):
            if secret[i] != guess[i]:
                if guess[i] in secretCounts.keys() and secretCounts[guess[i]] > 0:
                    cows += 1
                    secretCounts[guess[i]] -= 1
            
        ans = str(bulls) + 'A' + str(cows) + 'B'

        return ans