from collections import deque


# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # 非递归法
    # def flatten(self, root: TreeNode) -> None:
    #
    #     if not root:
    #         return
    #     stack = [root]
    #     pre = start = TreeNode(0)
    #     while stack:
    #         node = stack.pop()
    #         while node:
    #             pre.right = node
    #             pre = pre.right
    #             if node.right:
    #                 stack.append(node.right)
    #             node = node.left
    #             pre.left = None
    #             pre.right = None

    # 递归法，利用后序遍历

    def flatten(self, root: TreeNode) -> None:

        pre = None

        def dfs(root):
            if not root:
                return
            dfs(root.right)
            dfs(root.left)
            nonlocal pre
            root.right = pre
            root.left = None
            pre = root

        dfs(root)


# if __name__ == "__main__":
#     S = Solution()
#     print(S.isSameTree(nums1=[2], nums2=[]))
