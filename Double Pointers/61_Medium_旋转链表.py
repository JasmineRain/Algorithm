# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:

        # 先组成环并且计算长度，然后根据长度和k找到完成旋转后的链表头
        if not head:
            return head
        slow = fast = head
        length = 1
        while fast.next:
            fast = fast.next
            length += 1
        fast.next = head
        move = length - k % length - 1
        while move > 0:
            slow = slow.next
            move -= 1
        ans = slow.next
        slow.next = None
        return ans
