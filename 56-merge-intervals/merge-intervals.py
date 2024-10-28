class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        i = 0
        intervals.sort(key=lambda x: (x[0],[1]))
        while i < len(intervals) - 1:
            if intervals[i][1] >= intervals[i+1][0]:
                intervals[i+1][0] = min(intervals[i][0],intervals[i+1][0])
                intervals[i+1][1] = max(intervals[i][1],intervals[i+1][1])
                intervals.pop(i)
            else:
                i = i + 1
        return intervals