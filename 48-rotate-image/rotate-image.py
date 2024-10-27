class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(0,len(matrix)):
            for j in range(i+1, len(matrix)):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        for i in matrix:
            start = 0 
            end = len(matrix) - 1
            while start<end:
                temp = i[start]
                i[start] = i[end]
                i[end] = temp
                start = start + 1
                end = end - 1