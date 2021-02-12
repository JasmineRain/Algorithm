# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        dummy = ListNode(0)
        dummy.next = head

        pre = end = dummy
        move = k
        while end.next:
            while move > 0 and end:
                end = end.next
                move -= 1
            if not end:
                break
            start = pre.next
            post = end.next
            end.next = None
            pre.next = self.reverse(start)
            start.next = post
            pre = start
            end = pre
            move = k

        return dummy.next

    def reverse(self, start):
        pre = None
        cur = start
        while cur:
            post = cur.next
            cur.next = pre
            pre = cur
            cur = post
        return pre
