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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:

        if not inorder:
            return None

        root = TreeNode(postorder[-1])
        if len(postorder) == 1:
            return root
        skip = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:skip], postorder[: skip])
        root.right = self.buildTree(inorder[skip + 1:], postorder[skip: -1])
        return root

    # 迭代法
    # def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    #     if not preorder:
    #         return None


# if __name__ == "__main__":
#     S = Solution()
#     print(S.isSameTree(nums1=[2], nums2=[]))
