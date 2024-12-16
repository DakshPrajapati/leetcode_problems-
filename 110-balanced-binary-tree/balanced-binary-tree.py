# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True
        def trav(root):
            
            nonlocal balanced

            if not root:
                return 0
            hl = trav(root.left)
            hr = trav(root.right)

            if abs(hl- hr) > 1:
                balanced = False
                return 0

            return 1 + max(hl, hr)
        trav(root)
        return balanced 