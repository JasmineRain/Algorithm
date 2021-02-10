from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 递归法DFS
    # def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
    #     if not p and not q:
    #         return True
    #     elif p and q and p.val == q.val:
    #         return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    #     else:
    #         return False

    # 非递归法BFS
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False

        q1 = deque([p])
        q2 = deque([q])

        while q1 and q2:
            v1 = q1.popleft()
            v2 = q2.popleft()
            if v1.val != v2.val:
                return False
            if (not v1.left) ^ (not v2.left) or (not v1.right) ^ (not v2.right):
                return False
            if v1.left:
                q1.append(v1.left)
            if v1.right:
                q1.append(v1.right)
            if v2.left:
                q2.append(v2.left)
            if v2.right:
                q2.append(v2.right)

        return not q1 and not q2

# if __name__ == "__main__":
#     S = Solution()
#     print(S.isSameTree(nums1=[2], nums2=[]))
