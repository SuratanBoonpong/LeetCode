class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0
        while a>0 or b>0 or c>0:
            x1 = a & 1
            x2 = b & 1
            x3 = c & 1
            if (x1 or x2) != x3:
                if x1 and x2:
                    ans += 2
                else:
                    ans += 1
            a >>= 1
            b >>= 1
            c >>= 1
        return ans