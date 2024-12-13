# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        mDpth = 0
        dpth = 0
        def trav(root, dpth):
            nonlocal mDpth
            mDpth = max(mDpth, dpth)
            if not root:
                return
            trav(root.left, dpth + 1)
            trav(root.right, dpth + 1)
            
        trav(root, dpth)
        return mDpth