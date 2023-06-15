class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counts = 0
        for i in jewels:
            counts += stones.count(i)
        return counts