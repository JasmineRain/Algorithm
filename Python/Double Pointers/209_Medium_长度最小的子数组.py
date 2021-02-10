from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        fast = slow = 0
        total = 0
        length = float("inf")

        if sum(nums) < target:
            return 0

        while fast < len(nums):
            total += nums[fast]
            fast += 1

            while total >= target:
                length = min(length, fast - slow)
                total -= nums[slow]
                slow += 1

        return length


if __name__ == "__main__":
    S = Solution()
    print(S.minSubArrayLen(target=7, nums=[2, 3, 1, 2, 4, 3]))
