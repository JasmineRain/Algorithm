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
    def maxPathSum(self, root: TreeNode) -> int:

        ans = -float("inf")

        def dfs(root):
            if not root:
                return 0
            left_path = dfs(root.left)
            right_path = dfs(root.right)
            nonlocal ans
            ans = max(ans, root.val + max(0, left_path) + max(0, right_path))
            return root.val + max(left_path, right_path, 0)

        dfs(root)
        return ans


# if __name__ == "__main__":
#     S = Solution()
#     print(S.isSameTree(nums1=[2], nums2=[]))
