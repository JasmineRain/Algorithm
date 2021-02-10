# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        pre = ListNode()
        slow = head
        fast = head.next
        head = pre
        while slow is not None and fast is not None:
            slow.next = fast.next
            fast.next = slow
            pre.next = fast
            pre = pre.next.next
            slow = slow.next
            if slow is not None:
                fast = slow.next
        return head.next



