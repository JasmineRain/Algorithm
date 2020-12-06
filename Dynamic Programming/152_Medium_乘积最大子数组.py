from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        if not nums:
            return 0

        max_mul = [0] * len(nums)
        min_mul = [0] * len(nums)

        max_mul[0] = min_mul[0] = nums[0]

        for i in range(1, len(nums)):
            max_mul[i] = max(nums[i], max_mul[i - 1] * nums[i], min_mul[i - 1] * nums[i])
            min_mul[i] = min(nums[i], max_mul[i - 1] * nums[i], min_mul[i - 1] * nums[i])

        # print(max_mul)
        # print(min_mul)
        return max(max_mul)


if __name__ == "__main__":
    S = Solution()
    print(S.maxProduct(nums=[-2, 0, -1]))
