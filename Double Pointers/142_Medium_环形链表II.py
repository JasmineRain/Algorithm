from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = fast = ans = head
        flag = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                flag = True
                break

        if not flag:
            return

        while ans != slow:
            ans = ans.next
            slow = slow.next

        return ans
