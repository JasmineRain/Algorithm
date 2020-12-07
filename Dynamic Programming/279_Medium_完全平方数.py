import math


class Solution:
    def numSquares(self, n: int) -> int:

        square_nums = [i**2 for i in range(1, int(math.sqrt(n))+1)]
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            min_value = i
            for s in square_nums:
                if i < s:
                    break

                min_value = min(min_value, dp[i-s] + 1)
            dp[i] = min_value

        return dp[n]


if __name__ == "__main__":
    S = Solution()
    print(S.numSquares(n=13))
