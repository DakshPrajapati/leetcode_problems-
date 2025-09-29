class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(1, len(triangle)):
            for idx, v in enumerate(triangle[i]):
                v1 = triangle[i-1][idx] if idx < len(triangle[i-1]) else float('inf')
                v2 = triangle[i-1][idx-1] if idx - 1 >= 0 else float('inf')
                triangle[i][idx] = min(v1, v2) + v
        return min(triangle[-1])