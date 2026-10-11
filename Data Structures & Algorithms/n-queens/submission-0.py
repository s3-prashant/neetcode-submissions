class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        board = [["."]*n for _ in range(n)]
        res = []
        col = set()
        positiveDig = set()
        negativeDig = set()

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in col or (r+c) in positiveDig or (r-c) in negativeDig:
                    continue

                col.add(c)
                positiveDig.add(r+c)
                negativeDig.add(r-c)
                board[r][c] = "Q"

                backtrack(r+1)

                col.remove(c)
                positiveDig.remove(r+c)
                negativeDig.remove(r-c)
                board[r][c] = "."

        
        backtrack(0)
        return res         