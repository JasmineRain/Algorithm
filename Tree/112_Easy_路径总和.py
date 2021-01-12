from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:

        def backtrack(root, value):
            value += root.val
            if value == sum and not root.left and not root.right:
                return True
            if root.left:
                if backtrack(root.left, value):
                    return True
            if root.right:
                if backtrack(root.right, value):
                    return True

            return False

        if not root:
            return False
        return backtrack(root, 0)


# if __name__ == "__main__":
#     S = Solution()
#     print(S.isSameTree(nums1=[2], nums2=[]))
