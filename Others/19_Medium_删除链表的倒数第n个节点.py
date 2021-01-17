# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = slow = head
        inter = n
        while inter >= 0 and fast is not None:
            fast = fast.next
            inter -= 1

        if fast is None and inter != -1:
            return head.next

        while fast is not None:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return head


