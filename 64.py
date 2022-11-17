class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        numrows = len(grid)
        numcols = len(grid[0])
        for i in range(1,numrows,1):
            grid[i][0] += grid[i-1][0] 
        for j in range(1,numcols,1):
            grid[0][j] += grid[0][j-1]
        for i in range(1,numrows,1):
            for j in range(1,numcols,1):
                grid[i][j] += min(grid[i-1][j],grid[i][j-1])
        return grid[-1][-1]