# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        ans = slow = pre = ListNode(0)
        slow.next = head
        fast = head

        while fast:
            if fast.val >= x:
                pre = fast
                fast = fast.next
            else:
                if slow == pre:
                    slow.next = fast
                    slow = slow.next
                    pre = fast
                    fast = fast.next
                else:
                    pre.next = fast.next
                    fast.next = slow.next
                    slow.next = fast
                    fast = pre.next
                    slow = slow.next

        return ans.next

