class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        rows,cols = len(matrix),len(matrix)
        matrix.reverse()
        print(matrix)
        for i in range(rows):
            for j in range(i+1,rows):
                    temp = matrix[i][j]
                    matrix[i][j] =  matrix[j][i]
                    matrix[j][i] = temp

