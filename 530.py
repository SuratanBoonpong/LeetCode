# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.minVal = 10**5
        self.prevNode = None
        def inOrder(node):
            if node == None:
                return
            inOrder(node.left)
            if self.prevNode is not None:
                self.minVal = min(self.minVal,abs(node.val-self.prevNode.val))
            self.prevNode = node
            inOrder(node.right)
        inOrder(root)
        return self.minVal