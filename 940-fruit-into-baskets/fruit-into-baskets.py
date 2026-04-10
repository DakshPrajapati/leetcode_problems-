class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
   
        hashmap = defaultdict(int)
        seen = set()
        l = 0
        maxLen = 0

        for r, rightFruit in enumerate(fruits):
            seen.add(rightFruit)
            hashmap[rightFruit] += 1
            while len(seen) > 2:
                leftFruit = fruits[l]
                if hashmap[leftFruit] == 1:
                    seen.remove(leftFruit)
                hashmap[leftFruit] -= 1 if hashmap[leftFruit] > 0 else 0
                l += 1
            maxLen = max(maxLen, r - l + 1)  # r - l + 1 is current length
        
        return maxLen

