from typing import List


# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return
        return self.merge(lists, 0, len(lists) - 1)


    def merge(self, lists, left, right):
        if left == right:
            return lists[left]
        idx = left + (right - left) // 2
        l1 = self.merge(lists, left, idx)
        l2 = self.merge(lists, idx + 1, right)
        return self.merge_two_lists(l1, l2)

    def merge_two_lists(self, l1, l2):
        res = ListNode(0, None)
        head = res
        while l1 and l2:
            if l1.val < l2.val:
                res.next = l1
                l1 = l1.next
            else:
                res.next = l2
                l2 = l2.next
            res = res.next

        if l1:
            res.next = l1
        if l2:
            res.next = l2

        return head.next

# if __name__ == "__main__":
#     S = Solution()
#     print(S.mergeKLists(lists=[[1, 4, 5], [1, 3, 4], [2, 6]]))
#     print(S.mergeKLists(lists=[]))
#     print(S.mergeKLists(lists=[[]]))
