class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        currentRow = [1]
        for i in range(rowIndex):
            nextrow = []
            nextrow.append(1)
            for i in range(len(currentRow)-1):
                nextrow.append(currentRow[i]+currentRow[i+1])
            nextrow.append(1)
            currentRow = nextrow
        return currentRow