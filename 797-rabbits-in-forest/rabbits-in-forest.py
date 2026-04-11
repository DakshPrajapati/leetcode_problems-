class Solution:
    def numRabbits(self, answers: List[int]) -> int:

        hashMap = {}
        minNumber = 0

        for answer in answers:
            freq = hashMap.get(answer, 0)
            if freq == 0:
                minNumber += 1 + answer 
                hashMap[answer] = answer
            else:
                hashMap[answer] -= 1
        
        return (minNumber)