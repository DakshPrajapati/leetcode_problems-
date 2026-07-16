class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        heights.append(0)
        for idx, val in enumerate(heights):
            pos = idx
            while stack and stack[-1][0] > val:
                v, pos = stack.pop()
                area = v * (idx-pos)
                maxArea = max(maxArea, area) 
            stack.append([val, pos])
        return maxArea