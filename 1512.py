class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        repeats = {}
        num = 0
        for i in nums:
            if i in repeats:
                if repeats[i] == 1:
                    num += 1
                else:
                    num += repeats[i]
                repeats[i] += 1          
            else:
                repeats[i] = 1
        return num