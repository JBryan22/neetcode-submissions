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

        while pstack and qstack:
            pnode = pstack.pop()
            qnode = qstack.pop()

            if pnode.val != qnode.val:
                return False
            
            if pnode and qnode:
                pstack.append(pnode.left)
                pstack.append(pnode.right)
                qstack.append(qnode.left)
                qstack.append(qnode.right)
        return True