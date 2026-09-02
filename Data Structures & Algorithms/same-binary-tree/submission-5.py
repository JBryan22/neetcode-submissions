# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pstack = [p]
        qstack = [q]

        while pstack or qstack:
            if not pstack or not qstack:
                return False
            pnode = pstack.pop()
            qnode = qstack.pop()

            if not qnode and not pnode:
                continue
            if not qnode or not pnode:
                return False
            if pnode.val != qnode.val:
                return False
            
            pstack.append(pnode.left)
            pstack.append(pnode.right)
            qstack.append(qnode.left)
            qstack.append(qnode.right)
        return True