from typing import List


class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:

        ans = []

        def max_subseq(nums, k):
            ans = []
            rm = len(nums) - k
            for n in nums:
                while ans and rm > 0 and ans[-1] < n:
                    ans.pop()
                    rm -= 1
                ans.append(n)
            return ans[:k]

        def merge(a, b):
            res = []
            s1 = s2 = 0
            while s1 < len(a) and s2 < len(b):
                if a[s1:] > b[s2:]:
                    res.append(a[s1])
                    s1 += 1
                else:
                    res.append(b[s2])
                    s2 += 1
            res += a[s1:] if s2 == len(b) else b[s2:]
            return res

        for i in range(k + 1):
            if i <= len(nums1) and k - i <= len(nums2):
                ans = max(ans, merge(max_subseq(nums1, i), max_subseq(nums2, k - i)))
        return ans


if __name__ == "__main__":
    S = Solution()
    # print(S.maxNumber(nums1=[3, 4, 6, 5], nums2=[9, 1, 2, 5, 8, 3], k=5))
    print(S.maxNumber(nums1=[6, 7], nums2=[6, 0, 4], k=5))
