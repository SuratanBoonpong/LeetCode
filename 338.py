class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        num = 0
        start = [0,1]
        while(2**num<=n):
            num += 1
        num -= 2
        for i in range(num):
            count = len(start)
            for j in range(count):
                start.append(start[j]+1)
        for i in range(n+1-len(start)):
            start.append(start[i]+1)
        return start