from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        if not triangle:
            return 0

        nrow = len(triangle) + 1
        ncol = len(triangle) + 1

        # dp[i][j] 代表自顶向下到三角形第i行第j个元素的最小路径和，计数均从1开始
        dp = [[0 for _ in range(ncol)] for _ in range(nrow)]

        for i in range(1, nrow):
            for j in range(1, i + 1):

                if j == 1:
                    dp[i][j] = dp[i - 1][j] + triangle[i - 1][j - 1]
                elif j == i:
                    dp[i][j] = dp[i - 1][j - 1] + triangle[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i - 1][j - 1]

        return min(dp[len(triangle)][1:])

    def minimumTotal2(self, triangle: List[List[int]]) -> int:

        if not triangle:
            return 0

        nrow = len(triangle[-1])
        ncol = len(triangle[-1])

        # dp[i][j] 代表自底向上到三角形第i行第j个元素的最小路径和，计数均从0开始
        dp = [[0 for _ in range(ncol)] for _ in range(nrow)]
        dp[-1] = triangle[-1]
        for i in range(nrow - 2, -1, -1):
            for j in range(0, i + 1):
                dp[i][j] = min(dp[i + 1][j], dp[i + 1][j + 1]) + triangle[i][j]

        return dp[0][0]


if __name__ == "__main__":
    S = Solution()
    print(S.minimumTotal(triangle=[
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]))
    print(S.minimumTotal2(triangle=[
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]))
