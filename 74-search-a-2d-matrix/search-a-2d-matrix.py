class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(0, len(matrix)):
            if target >= matrix[i][0] and target <= matrix[i][-1]:
                for j in range(0, len(matrix[i])):
                    if target == matrix[i][j]:
                        return True
        return False 