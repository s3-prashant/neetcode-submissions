class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows,cols = len(matrix),len(matrix[0])
        
        zero_matrix = [[0]*i for i in range(len(matrix))]
        markr,markc = [False]*rows,[False]*cols

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                   markr [i]= True
                   markc[j] = True
        for i in range(rows):
            for j in range(cols):
                if markr[i] or markc[j]:
                    matrix[i][j] = 0
        
