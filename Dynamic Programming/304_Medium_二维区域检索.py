from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):

        if not matrix or not matrix[0]:
            pass
        else:
            nrow = len(matrix) + 1
            ncol = len(matrix[0]) + 1

            self.dp = [[0 for c in range(ncol)] for r in range(nrow)]

            for i in range(1, nrow):
                for j in range(1, ncol):
                    self.dp[i][j] = - self.dp[i - 1][j - 1] + self.dp[i][j - 1] + self.dp[i - 1][j] + matrix[i - 1][
                        j - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        return self.dp[row2 + 1][col2 + 1] - self.dp[row1][col2 + 1] - self.dp[row2 + 1][col1] + self.dp[row1][col1]


if __name__ == "__main__":
    S = NumMatrix(matrix=[
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5]
    ])

    print(S.sumRegion(1, 1, 2, 2))

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
