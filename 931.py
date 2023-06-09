class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        for i in range(1,len(matrix)):
            for j in range(0,len(matrix[i])):
                if j == 0:
                    matrix[i][j] = matrix[i][j]+min(matrix[i-1][j],matrix[i-1][j+1])
                elif j==len(matrix[i])-1:
                    matrix[i][j] = matrix[i][j]+min(matrix[i-1][j-1],matrix[i-1][j])
                else:
                    matrix[i][j] = matrix[i][j]+min(matrix[i-1][j-1],matrix[i-1][j],matrix[i-1][j+1])
        return min(matrix[-1])