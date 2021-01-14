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
    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        ans = 0

        def dfs(root):
            if not root:
                return 0
            left_length = dfs(root.left)
            right_length = dfs(root.right)
            nonlocal ans
            ans = max(ans, left_length + right_length)
            return 1 + max(left_length, right_length)

        dfs(root)
        return ans


# if __name__ == "__main__":
#     S = Solution()
#     print(S.isSameTree(nums1=[2], nums2=[]))
