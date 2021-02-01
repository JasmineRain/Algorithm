# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 空间复杂度O(n)
    # def isPalindrome(self, head: ListNode) -> bool:
    #     values = []
    #     while head:
    #         values.append(head.val)
    #         head = head.next
    #
    #     left, right = 0, len(values) - 1
    #     while left < right:
    #         if values[left] != values[right]:
    #             return False
    #         left += 1
    #         right -= 1
    #     return True

    # 空间复杂度O(1)
    def isPalindrome(self, head: ListNode) -> bool:
        def reverse(head):
            pre, cur = None, head
            while cur:
                third = cur.next
                cur.next = pre
                pre = cur
                cur = third
            return pre

        if not head:
            return True
        # 快慢指针寻找后半段链表
        pre, slow, fast = None, head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            pre = slow
            slow = slow.next
        if fast:
            pre = slow
            slow = slow.next
        # 翻转后半段
        last = right = reverse(slow)
        # 判断
        left = head
        while left and right:
            if left.val != right.val:
                pre.next = reverse(last)
                return False
            left = left.next
            right = right.next
        # 恢复原链表
        pre.next = reverse(last)
        return True