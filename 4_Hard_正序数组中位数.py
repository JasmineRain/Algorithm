from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        left = right = 0
        pre = now = 0
        length = len(nums1) + len(nums2)
        if length == 0:
            return 0
        count = 0
        while count <= length // 2:
            pre = now
            if left < len(nums1) and (right >= len(nums2) or nums1[left] <= nums2[right]):
                now = nums1[left]
                left += 1
            else:
                now = nums2[right]
                right += 1
            count += 1

        if length % 2 == 0:
            return (pre + now) / 2
        else:
            return now


if __name__ == "__main__":
    S = Solution()
    print(S.findMedianSortedArrays(nums1=[2], nums2=[]))
