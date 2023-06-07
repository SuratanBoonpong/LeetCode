class Solution:
    def countVowelStrings(self, n: int) -> int:
        startList = [1,1,1,1,1]
        for i in range(n-1):
            oldList = list(startList)
            for j in range(5):
                startList[j] += sum(oldList[:j])
        return sum(startList)

        #use Combinations with Repetition (n+r-1)c(r) 
        #n = number of elements
        #r = size of combination
        #return (n + 1) * (n + 2) * (n + 3) * (n + 4) / 24
