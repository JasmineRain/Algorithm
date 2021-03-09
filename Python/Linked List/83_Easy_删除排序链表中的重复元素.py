# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(float("inf"), None)
        slow = dummy
        fast = head
        while fast:
            if fast.val != slow.val:
                slow.next = fast
                slow = slow.next
                fast = fast.next
            else:
                slow.next = None
                fast = fast.next
        return dummy.next

