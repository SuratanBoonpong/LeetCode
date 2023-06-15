class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = rectangle
        self.history = []

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        self.history.append((row1,col1,row2,col2,newValue))

    def getValue(self, row: int, col: int) -> int:
        for i in list(reversed(self.history)):
            if i[0] <= row <= i[2] and i[1] <= col <= i[3]:
                return i[4]
        return self.rectangle[row][col]


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)