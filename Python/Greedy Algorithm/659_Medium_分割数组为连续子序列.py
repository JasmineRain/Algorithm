from collections import Counter
from typing import List


class Solution:
    def isPossible(self, nums: List[int]) -> bool:

        # remain 统计数字的剩余出现次数
        # exist  统计以某数字结尾的子序列数目
        remain = Counter(nums)
        exist = Counter()

        for i in range(len(nums)):

            if remain[nums[i]] <= 0:
                continue

            if exist.get(nums[i] - 1, 0) > 0:
                exist[nums[i] - 1] -= 1
                remain[nums[i]] -= 1
                exist[nums[i]] += 1
            else:
                if remain.get(nums[i] + 1, 0) <= 0 or remain.get(nums[i] + 2, 0) <= 0:
                    return False
                else:
                    remain[nums[i]] -= 1
                    remain[nums[i] + 1] -= 1
                    remain[nums[i] + 2] -= 1
                    exist[nums[i] + 2] += 1
        return True


if __name__ == "__main__":
    S = Solution()
    print(S.isPossible([1, 2, 3, 3, 4, 5]))
    print(S.isPossible([1, 2, 3, 3, 4, 4, 5, 5]))
    print(S.isPossible([1, 2, 3, 4, 4, 5]))
