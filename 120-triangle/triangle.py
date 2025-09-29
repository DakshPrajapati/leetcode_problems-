class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(1, len(triangle)):
            eles = triangle[i]
            for idx, v in enumerate(eles):
                v1, v2 = float('inf'), float('inf')
                if 0 <= idx < len(triangle[i-1]): v1 = triangle[i-1][idx]
                if 0 <= idx - 1 < len(triangle[i-1]): v2 = triangle[i-1][idx-1]
                triangle[i][idx] = min(v1, v2) + v
        return min(triangle[-1])