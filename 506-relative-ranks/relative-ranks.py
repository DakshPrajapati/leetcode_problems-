class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ranks = [-x for x in score]
        heapq.heapify(ranks)
        count = 0
        
        while ranks:
            rank = -heapq.heappop(ranks)
            count += 1
            for idx, s in enumerate(score):
                if s == rank:
                    score[idx] = str(count)
        
        medals = {
            '1': 'Gold Medal',
            '2': 'Silver Medal',
            '3': 'Bronze Medal'
        }

        tmp = 0
        for idx, rank in enumerate(score):
            if rank in medals.keys():
                score[idx] = medals[rank]
                tmp += 1
                if tmp >= 3:
                    break
        
        return (score)