class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        dp = [[[0] * (n + 2) for _ in range(m + 2)] for _ in range(N + 1)]
        for k in range(N + 1):
            for x in range(m + 2):
                for y in range(n + 2):
                    if x == 0 or x == m+1 or y == 0 or y == n+1:
                        dp[k][x][y] = 1
                    else:
                        if k == 0:
                            continue
                        else:
                            dp[k][x][y] = (dp[k-1][x][y-1] + dp[k-1][x][y+1] + dp[k-1][x-1][y] + dp[k-1][x+1][y]) % 1000000007
        return dp[N][i+1][j+1]


if __name__ == "__main__":
    S = Solution()
    print(S.findPaths(m=2, n=2, N=2, i=0, j=0))
