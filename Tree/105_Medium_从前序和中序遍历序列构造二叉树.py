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
    # def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    #
    #     if not preorder:
    #         return None
    #
    #     root = TreeNode(preorder[0])
    #     if len(preorder) == 1:
    #         return root
    #     skip = inorder.index(preorder[0])
    #     root.left = self.buildTree(preorder[1: skip + 1], inorder[:skip])
    #     root.right = self.buildTree(preorder[skip + 1:], inorder[skip + 1:])
    #     return root

    # 迭代法
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        stack = [root]
        inorder_idx = 0

        for i in range(1, len(preorder)):
            node = stack[-1]
            if node.val != inorder[inorder_idx]:
                node.left = TreeNode(preorder[i])
                stack.append(node.left)
            else:
                while stack and stack[-1].val == inorder[inorder_idx]:
                    node = stack.pop()
                    inorder_idx += 1
                node.right = TreeNode(preorder[i])
                stack.append(node.right)
        return root


# if __name__ == "__main__":
#     S = Solution()
#     print(S.isSameTree(nums1=[2], nums2=[]))
