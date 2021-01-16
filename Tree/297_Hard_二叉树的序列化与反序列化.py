# Definition for a binary tree node.
from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    # DFS 空格字符作为占位符，逗号作为分隔符
    # def serialize(self, root):
    #     # Encodes a tree to a single string.
    #     if not root:
    #         return " "
    #     left = self.serialize(root.left)
    #     right = self.serialize(root.right)
    #     return str(root.val) + "," + left + "," + right
    #
    # def deserialize(self, data):
    #     # Decodes your encoded data to tree.
    #
    #     def _decode(series):
    #         node = series.popleft()
    #         if node == " ":
    #             return None
    #         root = TreeNode(int(node))
    #         root.left = _decode(series)
    #         root.right = _decode(series)
    #         return root
    #
    #     return _decode(deque(data.split(",")))


    # BFS
    def serialize(self, root):
        # Encodes a tree to a single string.
        queue = deque([root])
        res = []
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append(' ')

        return ",".join(res)


    def deserialize(self, data):
        # Decodes your encoded data to tree.
        if data == " ":
            return None
        series = data.split(",")
        root = TreeNode(int(series[0]))
        queue = deque([root])
        idx = 1

        while idx < len(series):
            node = queue.popleft()

            left = series[idx]
            right = series[idx + 1]

            if left != " ":
                left_node = TreeNode(int(left))
                node.left = left_node
                queue.append(left_node)

            if right != " ":
                right_node = TreeNode(int(right))
                node.right = right_node
                queue.append(right_node)

            idx += 2

        return root
