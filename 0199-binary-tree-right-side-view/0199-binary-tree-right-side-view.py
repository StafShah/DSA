# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        rsv = [root]
        found = False
        q = collections.deque()
        q.append(root)
        currLevel = 1

        
        while q:
            print(currLevel)
            n = q.popleft()
            currLevel -= 1

            if n.right:
                if found == False:
                    rsv.append(n.right)
                    found = True
                q.append(n.right)
            if n.left:
                if found == False:
                    rsv.append(n.left)
                    found = True
                q.append(n.left)

            if currLevel == 0:
                currLevel = len(q)
                found = False
            
        return [node.val for node in rsv]