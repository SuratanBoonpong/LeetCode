class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxVal = 0
        currentVal = 0
        for i in gain:
            currentVal += i
            maxVal = max(maxVal,currentVal)
        return maxVal