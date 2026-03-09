# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque()
        q.append(root)
        levels = []
        while q:
            level = []
            for i in range(len(q)):
                x = q.popleft()
                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)
                level.append(x.val)
            levels.append(level)
        return levels