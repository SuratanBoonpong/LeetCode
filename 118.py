class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = [[1]]
        for i in range(numRows-1):
            currentRow = output[-1]
            nextrow = []
            nextrow.append(1)
            for i in range(len(currentRow)-1):
                nextrow.append(currentRow[i]+currentRow[i+1])
            nextrow.append(1)
            output.append(nextrow)
        return output