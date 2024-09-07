# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkBST(self, root, minVal, maxVal):
        if root is None:
            return True

        if not (minVal < root.val < maxVal):
            return False

        if root.left:
            l = self.checkBST(root.left, minVal, root.val)
        else:
            l = True

        if root.right:
            r = self.checkBST(root.right, root.val, maxVal)
        else:
            r = True

        return l and r

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.checkBST(root, float('-inf'), float('inf'))
