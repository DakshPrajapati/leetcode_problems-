# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1
        q = deque()
        q.append(root)
        ans, level = 0, 0
        curMax = -float('inf')
        while q:
            total = 0
            level += 1
            for i in range(len(q)):
                x = q.popleft()
                total += x.val
                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)
            if total > curMax:
                curMax = total
                ans = level
        return ans