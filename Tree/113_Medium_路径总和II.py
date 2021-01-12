from collections import deque


# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:

        ans = []

        def backtrack(root, value, trace):
            value += root.val
            if value == sum and not root.left and not root.right:
                ans.append(trace + [root.val])
                return
            if root.left:
                backtrack(root.left, value, trace + [root.val])
            if root.right:
                backtrack(root.right, value, trace + [root.val])

        if not root:
            return []
        backtrack(root, 0, [])
        return ans


# if __name__ == "__main__":
#     S = Solution()
#     print(S.isSameTree(nums1=[2], nums2=[]))
