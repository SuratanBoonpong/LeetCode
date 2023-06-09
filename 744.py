class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        #use binary-search
        left = 0
        right = len(letters) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

        if left < len(letters):
            return letters[left]  
        else:
            return letters[0]