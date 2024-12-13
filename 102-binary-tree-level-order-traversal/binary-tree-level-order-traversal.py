# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = defaultdict(list)
        dpth = 0
        def trav(root, dpth):   
            if not root:
                return 
            res[dpth].append(root.val)
            trav(root.left, dpth+1)
            trav(root.right, dpth+1)
        trav(root, dpth)
        return list(res.values())
