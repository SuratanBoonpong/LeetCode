class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        matrix = [[int(num) for num in row] for row in matrix]
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[i])):
                matrix[i][j] += (min(matrix[i-1][j],matrix[i-1][j-1],matrix[i][j-1])*matrix[i][j])
        return max([max(item) for item in matrix])**2