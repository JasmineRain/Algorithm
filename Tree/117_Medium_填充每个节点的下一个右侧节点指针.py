from typing import List
from collections import deque


# Definition for a binary tree node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    # BFS
    # def connect(self, root: 'Node') -> 'Node':
    #     if not root:
    #         return
    #     queue = deque([root])
    #     while queue:
    #         count = len(queue)
    #         while count > 0:
    #             node = queue.popleft()
    #             if count == 1:
    #                 node.next = None
    #             else:
    #                 node.next = queue[0]
    #             if node.left:
    #                 queue.append(node.left)
    #             if node.right:
    #                 queue.append(node.right)
    #             count -= 1
    #     return root

    # BFS 2
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        cur = root

        while cur:
            start = Node(0)
            tail = start
            while cur:
                if cur.left:
                    tail.next = cur.left
                    tail = tail.next
                if cur.right:
                    tail.next = cur.right
                    tail = tail.next
                cur = cur.next
            cur = start.next

        return root
