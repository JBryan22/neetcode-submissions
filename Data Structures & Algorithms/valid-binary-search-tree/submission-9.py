# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def validDfs(root: Optional[TreeNode], min, max) -> bool:
            if not root:
                return True
            return (root.val > min 
                    and root.val < max 
                    and validDfs(root.left, min, root.val)
                    and validDfs(root.right, root.val, max))
                    
        return validDfs(root, -math.inf, math.inf)