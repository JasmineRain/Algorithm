from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        if not nums:
            pass
        else:
            self.nums = nums
            self.dp = [0] * len(nums)
            self.dp[0] = nums[0]
            for i in range(1, len(nums)):
                self.dp[i] = self.dp[i-1] + nums[i]

    def sumRange(self, i: int, j: int) -> int:

        return self.dp[j] - self.dp[i] + self.nums[i]


if __name__ == "__main__":
    S = NumArray(nums=[-2, 0, 3, -5, 2, -1])
    print(S.sumRange(0, 5))

