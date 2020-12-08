class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:

        if n <= 1:
            return 10 ** n

        num = 0
        dp = [1] * (n + 1)
        dp[1] = 9
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] * (10 - i + 1)
            num += dp[i]
        return num + 10


if __name__ == "__main__":
    S = Solution()
    print(S.countNumbersWithUniqueDigits(n=2))
