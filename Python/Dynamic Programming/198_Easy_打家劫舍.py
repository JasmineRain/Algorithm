from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) < 1:
            return 0

        dp = [[0, 0] for _ in range(len(nums))]
        dp[0][0] = 0
        dp[0][1] = nums[0]

        for i in range(1, len(nums)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
            dp[i][1] = dp[i - 1][0] + nums[i]

        return max(dp[len(nums) - 1][0], dp[len(nums) - 1][1])


if __name__ == "__main__":
    S = Solution()
    print(S.rob(nums=[1]))
