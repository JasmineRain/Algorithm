# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return
        ans = root
        while True:
            if ans.val < p.val and ans.val < q.val:
                ans = ans.right
            elif ans.val > p.val and ans.val > q.val:
                ans = ans.left
            else:
                break
        return ans
