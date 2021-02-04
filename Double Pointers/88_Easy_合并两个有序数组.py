from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left, right, pos = m - 1, n - 1, m + n - 1
        while left >= 0 and right >= 0:
            n1 = nums1[left]
            n2 = nums2[right]
            if n1 <= n2:
                nums1[pos] = n2
                right -= 1
            else:
                nums1[pos] = n1
                left -= 1
            pos -= 1
        if left < 0:
            nums1[: pos + 1] = nums2[: right + 1]
        # else:
        #     nums1[: pos + 1] = nums1[: left + 1]


if __name__ == "__main__":
    S = Solution()
    print(S.merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3))
