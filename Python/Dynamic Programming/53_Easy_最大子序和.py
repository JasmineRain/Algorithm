from typing import List


class Solution:
    # 动态规划解法，dp[i]代表到s[i]的最大子序和，状态转移由左元素得到
    # 注意状态图维度的选取
    def maxSubArray(self, nums: List[int]) -> int:
        size = len(nums)
        dp = [0 for _ in range(size)]

        if size == 0:
            return 0

        for i in range(0, size):
            if i == 0:
                dp[i] = nums[i]
            else:
                dp[i] = max(dp[i-1] + nums[i], nums[i])
        return max(dp)


if __name__ == "__main__":
    S = Solution()
    print(S.maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    # -2, 1, -3, 4, -1, 2, 1, -5, 4
