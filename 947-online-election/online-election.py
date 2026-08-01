class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.votes = defaultdict(int)
        self.voteAtTime = {}
        self.curMax= -float('inf')
    
        for i in range(len(persons)):
            self.insert(persons[i], times[i])
            
    def insert(self, p: int, t: int):
        self.votes[p] += 1
        if self.votes[p] >= self.curMax:
            self.voteAtTime[t] = p
            self.curMax = self.votes[p] 

    def q(self, t: int) -> int:
        ans = 0
        for ti in self.voteAtTime:
            if ti > t:
                return ans    
            ans = self.voteAtTime[ti]
        return ans

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)