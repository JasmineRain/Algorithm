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
    # def convertBST(self, root: TreeNode) -> TreeNode:
    #
    #     total = 0
    #
    #     def dfs(root):
    #         if not root:
    #             return
    #         dfs(root.right)
    #         nonlocal total
    #         total += root.val
    #         root.val = total
    #         dfs(root.left)
    #
    #     dfs(root)
    #     return root

    # 非递归法
    def convertBST(self, root: TreeNode) -> TreeNode:

        stack = deque()
        total = 0
        start = root
        if not root:
            return

        while root or stack:
            while root:
                stack.append(root)
                root = root.right

            root = stack.pop()
            total += root.val
            root.val = total
            root = root.left

        return start


# if __name__ == "__main__":
#     S = Solution()
#     print(S.isSameTree(nums1=[2], nums2=[]))
