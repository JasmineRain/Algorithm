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
    # def postorderTraversal(self, root: TreeNode) -> List[int]:
    #
    #     res = []
    #
    #     def dfs(root):
    #         if not root:
    #             return
    #         dfs(root.left)
    #         dfs(root.right)
    #         res.append(root.val)
    #
    #     dfs(root)
    #     return res

    # 非递归法
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = deque()
        prev = None
        if not root:
            return res

        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            if not root.right or root.right == prev:
                res.append(root.val)
                prev = root
                root = None
            else:
                stack.append(root)
                root = root.right

        return res


# if __name__ == "__main__":
#     S = Solution()
#     print(S.isSameTree(nums1=[2], nums2=[]))
