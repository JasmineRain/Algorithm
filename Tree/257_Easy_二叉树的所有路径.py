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
    # def binaryTreePaths(self, root: TreeNode) -> List[str]:
    #
    #     res = []
    #     def backtrack(root, trace):
    #         if not root:
    #             return
    #         trace.append(str(root.val))
    #         if not root.left and not root.right:
    #             res.append(trace.copy())
    #         backtrack(root.left, trace)
    #         backtrack(root.right, trace)
    #         trace.pop()
    #
    #     backtrack(root, [])
    #     for i in range(len(res)):
    #         res[i] = "->".join(res[i])
    #
    #     return res

    # BFS
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []

        if not root:
            return res

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
                    paths.append(path + "->" + str(node.left.val))
                if node.right:
                    nodes.append(node.right)
                    paths.append(path + "->" + str(node.right.val))

        return res


# if __name__ == "__main__":
#     S = Solution()
#     print(S.isSameTree(nums1=[2], nums2=[]))
