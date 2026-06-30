# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        s1, s2 = [p], [q]
        while s1 or s2:
            if not s1 or not s2:
                return False
            s1Node = s1.pop()
            s2Node = s2.pop()

            if not s1Node and not s2Node:
                continue
            if not s1Node or not s2Node:
                return False

            if s1Node.val != s2Node.val:
                return False
            
            s1.append(s1Node.left)
            s1.append(s1Node.right)
            s2.append(s2Node.left)
            s2.append(s2Node.right)
        return True
            