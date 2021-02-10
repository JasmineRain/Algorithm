from typing import List
from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)

        ans = []
        exist = Counter(nums1)

        for num in nums2:
            if num in exist:
                ans.append(num)
                exist[num] -= 1
                if exist[num] == 0:
                    exist.pop(num)
        return ans


if __name__ == "__main__":
    S = Solution()
    print(S.intersect(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]))
