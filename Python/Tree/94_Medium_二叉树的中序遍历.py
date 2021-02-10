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
    # def inorderTraversal(self, root: TreeNode) -> List[int]:
    #
    #     res = []
    #
    #     def dfs(root):
    #         if not root:
    #             return
    #         dfs(root.left)
    #         res.append(root.val)
    #         dfs(root.right)
    #
    #     dfs(root)
    #     return res

    # 非递归法
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        res = []
        stack = deque()
        if not root:
            return res

        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            res.append(root.val)
            root = root.right

        return res


# if __name__ == "__main__":
#     S = Solution()
#     print(S.isSameTree(nums1=[2], nums2=[]))
