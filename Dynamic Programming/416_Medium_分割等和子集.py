from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # 定义dp[i][j]为前i个元素是否能凑出j值
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        dp = [[False for _ in range(target + 1)] for _ in range(len(nums) + 1)]
        dp[0][0] = True
        for i in range(1, target + 1):
            dp[0][i] = False
        for i in range(1, len(nums) + 1):
            dp[i][0] = False
        for i in range(1, len(nums) + 1):
            for j in range(1, target + 1):

                dp[i][j] = dp[i - 1][j]

                if nums[i-1] == j:
                    dp[i][j] = True
                elif nums[i-1] < j:
                    dp[i][j] = dp[i][j] or dp[i-1][j-nums[i-1]]

        # for i in range(0, len(nums) + 1):
        #     print(dp[i])
        return dp[-1][target]


if __name__ == "__main__":
    S = Solution()
    print(S.canPartition(nums=[1, 2, 3, 4, 5, 6, 7]))
