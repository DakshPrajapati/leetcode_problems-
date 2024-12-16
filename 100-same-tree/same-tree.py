# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        ifSame = True
        def trav(p, q):
            nonlocal ifSame
            if not p and not q:
                return
            if not p and q:
                ifSame = False
                return
            if not q and p:
                ifSame = False
                return 
            if p.val != q.val:
                ifSame = False
            trav(p.left, q.left)
            trav(p.right, q.right)
        trav(p,q)
        return ifSame