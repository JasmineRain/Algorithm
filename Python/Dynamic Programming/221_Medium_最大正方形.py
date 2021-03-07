from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        if not matrix:
            return 0

        nrow = len(matrix)
        ncol = len(matrix[0])
        max_value = 0

        dp = [[0 for _ in range(ncol)] for _ in range(nrow)]

        for i in range(0, nrow):
            for j in range(0, ncol):
                if matrix[i][j] == "0":
                    dp[i][j] = 0
                else:
                    if i == 0 or j == 0:
                        dp[i][j] = int(matrix[i][j])
                    else:
                        dp[i][j] = min(int(dp[i - 1][j - 1]), int(dp[i - 1][j]), int(dp[i][j - 1])) + 1
                max_value = dp[i][j] if dp[i][j] >= max_value else max_value

        return max_value ** 2


if __name__ == "__main__":
    S = Solution()
    print(S.maximalSquare(matrix=[["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"],
                                  ["1", "0", "0", "1", "0"]]))
