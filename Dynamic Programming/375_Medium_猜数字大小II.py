class Solution:
    def getMoneyAmount(self, n: int) -> int:
        # 定义dp为范围[i, j]内， 至少需要dp[i][j]金币才能确保结束游戏
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        for i in range(n, 0, -1):
            for j in range(i, n + 1):
                if i == j:
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(k + max(dp[i][k-1], dp[k+1][j]) for k in range(i, j))

        print(dp)
        return dp[1][n]

    def getMoneyAmount2(self, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(1, n):
            dp[i][i + 1] = i
        for low in range(n - 1, 0, -1):
            for high in range(low + 1, n + 1):
                dp[low][high] = min(x + max(dp[low][x - 1], dp[x + 1][high]) for x in range(low, high))
        print(dp)
        return dp[1][n]


if __name__ == "__main__":
    S = Solution()
    # for l in range(2, 6):
    #     for i in range(0, 5 - l + 1):
    #         print(i, l + i - 1)
    print(S.getMoneyAmount(5))
    print(S.getMoneyAmount2(5))
