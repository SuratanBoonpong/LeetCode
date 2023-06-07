class Solution:
    def countVowelStrings(self, n: int) -> int:
        startList = [1,1,1,1,1]
        for i in range(n-1):
            oldList = list(startList)
            for j in range(5):
                startList[j] += sum(oldList[:j])
        return sum(startList)