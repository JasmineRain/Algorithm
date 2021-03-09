from typing import List
from collections import Counter


class Solution:

    # 哈希
    def longestConsecutive(self, nums: List[int]) -> int:
        exist = Counter(nums)
        ans = 0
        for num in nums:
            if num - 1 in exist:
                continue
            else:
                cur = num
                length = 0
                while cur in exist:
                    length += 1
                    cur += 1
                ans = max(ans, length)
        return ans


if __name__ == "__main__":
    S = Solution()
    print(S.longestConsecutive(nums=[100, 4, 200, 1, 3, 2]))
    print(S.longestConsecutive(nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
