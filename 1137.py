class Solution:
    def tribonacci(self, n: int) -> int:
        tribo = [0,1,1]
        if n<3:
            return tribo[n]
        for i in range(3,n+1,1):
            tribo.append(tribo[-1]+tribo[-2]+tribo[-3])
        return tribo[-1]