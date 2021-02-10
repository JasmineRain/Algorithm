from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        ballon = [1] + nums + [1]

        # 定义dp[i][j]为开区间(i, j)内，能获得的最大硬币数
        dp = [[0 for _ in range(len(nums) + 2)] for _ in range(len(nums) + 2)]

        for i in range(len(nums) + 1, -1, -1):
            for j in range(i + 1, len(nums) + 2):
                if j == i + 1:
                    dp[i][j] = 0
                else:
                    for k in range(i + 1, j):
                        dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + ballon[i] * ballon[k] * ballon[j])

        return dp[0][-1]


if __name__ == "__main__":
    S = Solution()
    print(S.maxCoins(nums=[3, 1, 5, 8]))
