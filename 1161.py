# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        levelNode = [root]
        maxVal = float('-inf')
        maxLevel = 1
        self.currentLevel = 0
        while levelNode:
            sumval = 0
            self.currentLevel += 1
            nextLevelNode = []
            for node in levelNode:
                if node.left:
                    nextLevelNode.append(node.left)
                if node.right:
                    nextLevelNode.append(node.right)
                sumval += node.val
            if sumval > maxVal:
                maxVal = sumval
                maxLevel = self.currentLevel
            levelNode = nextLevelNode
    
        return maxLevel
                