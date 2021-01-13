from collections import deque

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # 递归法
    def isValidBST(self, root: TreeNode) -> bool:
        def dfs(root, min, max):
            if not root:
                return True

            if root.val >= max or root.val <= min:
                return False
            if not dfs(root.left, min, root.val):
                return False
            if not dfs(root.right, root.val, max):
                return False
            return True

        return dfs(root, -float("inf"), float("inf"))

    # 迭代法
    # def isValidBST(self, root: TreeNode) -> bool:

# if __name__ == "__main__":
#     S = Solution()
#     print(S.isSameTree(nums1=[2], nums2=[]))
