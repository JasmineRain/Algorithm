from collections import deque

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # DFS
    # def sumNumbers(self, root: TreeNode) -> int:
    #
    #     res = []
    #     def backtrack(root, trace):
    #         if not root:
    #             return
    #         if not root.left and not root.right:
    #             res.append(trace * 10 + root.val)
    #         backtrack(root.left, trace * 10 + root.val)
    #         backtrack(root.right, trace * 10 + root.val)
    #
    #     backtrack(root, 0)
    #
    #     return sum(res)

    # BFS
    def sumNumbers(self, root: TreeNode) -> int:
        res = []
        ans = 0
        if not root:
            return ans

        nodes = deque([root])
        paths = deque([str(root.val)])

        while nodes:
            node = nodes.popleft()
            path = paths.popleft()
            if not node.left and not node.right:
                res.append(path)
            else:
                if node.left:
                    nodes.append(node.left)
                    paths.append(path + str(node.left.val))
                if node.right:
                    nodes.append(node.right)
                    paths.append(path + str(node.right.val))

        for item in res:
            ans += int(item)
        return ans


# if __name__ == "__main__":
#     S = Solution()
#     print(S.isSameTree(nums1=[2], nums2=[]))
