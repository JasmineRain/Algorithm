# Definition for singly-linked list.
from collections import Counter


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(0, head)
        slow = dummy
        fast = head
        while fast:
            count = 0
            temp = fast
            while temp and temp.val == fast.val:
                temp = temp.next
                count += 1
            if count > 1:
                slow.next = temp
            else:
                slow = fast
            fast = temp

        return dummy.next


