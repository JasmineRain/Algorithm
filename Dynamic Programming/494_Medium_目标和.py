from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        # 定义dp[i][j]为前i个元素能凑出j值的方法数

        total = sum(abs(item) for item in nums)
        if total < S:
            return 0

        dp = [[0 for _ in range(2 * total + 1)] for _ in range(len(nums))]

        if nums[0] == 0:
            dp[0][total] = 2
        else:
            dp[0][total - nums[0]] = dp[0][total + nums[0]] = 1

        for i in range(1, len(nums)):
            for j in range(0, 2 * total + 1):
                left = max(0, j - nums[i])
                right = min(2 * total, j + nums[i])
                dp[i][j] = dp[i - 1][left] + dp[i - 1][right]

        for i in range(0, len(nums)):
            print(dp[i])
        return dp[-1][total+S]


if __name__ == "__main__":
    S = Solution()
    print(S.findTargetSumWays(nums=[1, 1, 1, 1, 1], S=3))
