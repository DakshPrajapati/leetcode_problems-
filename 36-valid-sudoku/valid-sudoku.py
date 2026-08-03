class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
       
        row = defaultdict(list)
        col = defaultdict(list)
        square = defaultdict(list)

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    x = board[i][j]
                    
                    if x in row[i]: return False
                    if x in col[j]: return False 
                    if x in square[(i//3, j//3)]: return False 
                
                    row[i].append(x)
                    col[j].append(x)
                    square[(i//3, j//3)].append(x)

        return True
