class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        rows,cols = len(matrix) , len(matrix[0])

        markr,markc = [False]* rows, [False]*cols

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    markr[r] = True
                    markc[c] = True
        
        for r in range(rows):
            for c in range(cols):
                if markr[r] or markc[c]:
                    matrix[r][c] = 0

        # def dfs(r,c):
        #     if r > rows or c > cols or matrix [r][c] == 0:
        #         return
            
        #     matrix[r][c] = 0
        #     dfs(r,c+1)
        #     dfs(r,c-1)
        #     dfs(r-1,c)
        #     dfs(r+1,c)



        # for r in range(rows):
        #     for c in range(cols):
        #         if matrix[r][c] == 0:
        #             dfs(r,c)