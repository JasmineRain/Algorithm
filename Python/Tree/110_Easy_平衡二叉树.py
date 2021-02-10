from collections import deque

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # 自底向上递归法
    def isBalanced(self, root: TreeNode) -> bool:

        # 如果左右子树不平衡，则返回-1，否则，返回左右子树最大高度
        def height(root):
            if not root:
                return 0

            left = height(root.left)
            right = height(root.right)

            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            else:
                return 1 + max(left, right)

        return height(root) >= 0

# if __name__ == "__main__":
#     S = Solution()
#     print(S.isSameTree(nums1=[2], nums2=[]))
