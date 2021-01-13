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
    # def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
    #
    #     if not inorder:
    #         return None
    #
    #     root = TreeNode(postorder[-1])
    #     if len(postorder) == 1:
    #         return root
    #     skip = inorder.index(postorder[-1])
    #     root.left = self.buildTree(inorder[:skip], postorder[: skip])
    #     root.right = self.buildTree(inorder[skip + 1:], postorder[skip: -1])
    #     return root

    # 迭代法
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return None
        root = TreeNode(postorder[-1])
        stack = [root]
        inorder_idx = len(postorder) - 1

        for i in range(len(postorder) - 2, -1, -1):
            node = stack[-1]
            if node.val != inorder[inorder_idx]:
                node.right = TreeNode(postorder[i])
                stack.append(node.right)
            else:
                while stack and stack[-1].val == inorder[inorder_idx]:
                    node = stack.pop()
                    inorder_idx -= 1
                node.left = TreeNode(postorder[i])
                stack.append(node.left)
        return root


# if __name__ == "__main__":
#     S = Solution()
#     print(S.isSameTree(nums1=[2], nums2=[]))
