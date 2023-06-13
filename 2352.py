from collections import defaultdict
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:  
        count = 0
        CountRow = defaultdict(int)
        for row in grid:
            CountRow[tuple(row)] += 1
        for col in zip(*grid):
            count += CountRow[col]
        return count