class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        subtractionList = {}
        for i in range(len(nums)):
            if target - nums[i] in subtractionList:
                return [subtractionList[target-nums[i]],i]
            subtractionList[nums[i]] = i
        return []