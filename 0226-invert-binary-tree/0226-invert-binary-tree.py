# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        if root.left and (root.left.left or root.left.right):
                root.left = self.invertTree(root.left)
        
        if root.right and (root.right.left or root.right.right):
                root.right = self.invertTree(root.right)
        
        placeholder = root.right
        root.right = root.left
        root.left = placeholder

        return root