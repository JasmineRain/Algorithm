from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1 = set(nums1)
        s2 = set(nums2)

        if len(s1) <= len(s2):
            return [item for item in s1 if item in s2]
        else:
            return [item for item in s2 if item in s1]


if __name__ == "__main__":
    S = Solution()
    print(S.intersection(nums1=[1, 2, 2, 1], nums2=[2, 2]))
