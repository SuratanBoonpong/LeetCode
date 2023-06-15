class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        leftArr = nums[:n]
        rightArr = nums[-n:]
        output = []
        for i in range(n):
            output.append(leftArr[i])
            output.append(rightArr[i])
        return output