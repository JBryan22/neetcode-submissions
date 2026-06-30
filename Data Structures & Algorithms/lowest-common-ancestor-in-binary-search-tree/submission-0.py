# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        pSet = set()

        def find(root, target, s1: Optional[set] = None) -> Optional[TreeNode]:
            if not root:
                return None
            if s1 and root.val in s1:
                return root

            pSet.add(root.val)

            if root.val == target.val:
                return None

            if root.left:
                find(root.left, target, s1)
            if root.right:
                find(root.right, target, s1)

        find(root, p)
        res = find(root, q, pSet)
        if res:
            return res
        else:
            return TreeNode()
            
            