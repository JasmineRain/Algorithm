from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 递归法DFS
    # def isSymmetric(self, root: TreeNode) -> bool:
    #
    #     if not root:
    #         return True
    #     if (not root.left) ^ (not root.right):
    #         return False
    #
    #     return self.checkSymmetric(root.left, root.right)
    #
    # def checkSymmetric(self, left, right):
    #     if not left and not right:
    #         return True
    #     if (not left) ^ (not right):
    #         return False
    #     return left.val == right.val and self.checkSymmetric(left.left, right.right) and self.checkSymmetric(left.right, right.left)



    # 非递归法BFS
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root or (not root.left and not root.right):
            return True

        queue = deque([root.left, root.right])

        while queue:
            left = queue.pop()
            right = queue.pop()

            if not left and not right:
                continue
            if not (left and right) or left.val != right.val:
                return False
            queue.append(left.left)
            queue.append(right.right)
            queue.append(left.right)
            queue.append(right.left)

        return True


# if __name__ == "__main__":
#     S = Solution()
#     print(S.isSameTree(nums1=[2], nums2=[]))
