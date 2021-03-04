from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_flag = False
        col_flag = False
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                col_flag = True
                break
        for i in range(len(matrix[0])):
            if matrix[0][i] == 0:
                row_flag = True
                break
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if row_flag:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0
        if col_flag:
            for i in range(len(matrix)):
                matrix[i][0] = 0


if __name__ == "__main__":
    S = Solution()
    arr = [
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5]
    ]
    S.setZeroes(arr)
    print(arr)
