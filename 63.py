class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        numrows = len(obstacleGrid)
        numcols = len(obstacleGrid[0])
        
        if obstacleGrid[0][0] == 1:
            return 0
        
        obstacleGrid[0][0] = 1
        for i in range(1,numrows):
            obstacleGrid[i][0] = int(obstacleGrid[i-1][0] == 1 and obstacleGrid[i][0] == 0)

        for i in range(1,numcols):
            obstacleGrid[0][i] = int(obstacleGrid[0][i-1] == 1 and obstacleGrid[0][i] == 0)

        for i in range(1,numrows):
            for j in range(1,numcols):
                obstacleGrid[i][j] = (obstacleGrid[i][j-1] + obstacleGrid[i-1][j]) * int(obstacleGrid[i][j] == 0)  
        return obstacleGrid[-1][-1]