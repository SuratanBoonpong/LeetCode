class SnapshotArray:

    def __init__(self, length: int):
        self.currentID = 0
        self.currentSnapshot = [0] * length
        self.snapshotValueHistory = [[0] for i in range(length)]
        self.snapshotIDHistory = [[-1] for i in range(length)]
        self.modified = set()

    def set(self, index: int, val: int) -> None:
        if val == self.snapshotValueHistory[index][-1]:
            if index in self.modified:
                self.modified.remove(index)
                return
        self.currentSnapshot[index] = val
        if index not in self.modified:
            self.modified.add(index)

    def printAll(self) -> None:
        print(self.currentID)
        print(self.currentSnapshot)
        print(self.snapshotIDHistory)
        print(self.snapshotValueHistory)
        print(self.modified)

obj = SnapshotArray(3)
obj.set(0,2)
obj.printAll()
obj.set(0,2)
obj.printAll()