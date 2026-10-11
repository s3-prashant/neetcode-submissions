class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        
        for i in range(len(board)):
            visit = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                
                
                if board[i][j] in visit:
                    return False
                visit.add(board[i][j])
            
                print(visit)
        for col in range(9):
            visit = set()
            for i in range(9):
                if board[i][col] == ".":
                    continue

                if board[i][col] in visit:
                    return False
                visit.add(board[i][col])
            
                print(visit)
        for square in range(9):
            visit = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue

                    if board[row][col] in visit:
                        return False
                    visit.add(board[row][col])
            
                print(visit)
            
        return True
