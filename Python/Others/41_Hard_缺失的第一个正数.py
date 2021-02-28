from typing import List


class Solution:

    # 原地哈希
    def firstMissingPositive(self, nums: List[int]) -> int:
        length = len(nums)

        for i in range(length):
            if nums[i] <= 0:
                nums[i] = length + 1

        for i in range(length):
            raw = abs(nums[i])
            if raw <= length:
                nums[raw - 1] = -abs(nums[raw - 1])

        for i in range(length):
            if nums[i] > 0:
                return i + 1
        return length + 1


if __name__ == "__main__":
    S = Solution()
    print(S.firstMissingPositive(nums=[1, 2, 0]))
    print(S.firstMissingPositive(nums=[3, 4, -1, 1]))
    print(S.firstMissingPositive(nums=[7, 8, 9, 11, 12]))
