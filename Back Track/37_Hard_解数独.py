from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        block_flag = [[[False for _ in range(9)] for _ in range(3)] for _ in range(3)]
        row_flag = [[False for _ in range(9)] for _ in range(9)]
        col_flag = [[False for _ in range(9)] for _ in range(9)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                else:
                    num = int(board[i][j]) - 1
                    row_flag[i][num] = True
                    col_flag[j][num] = True
                    block_flag[i // 3][j // 3][num] = True

        def backtrack(row, col):
            if col == len(board[0]):
                col = 0
                row += 1
                if row == len(board):
                    return True

            if board[row][col] != ".":
                return backtrack(row, col + 1)
            else:
                for i in range(1, 10):
                    if block_flag[row // 3][col // 3][i - 1] or row_flag[row][i - 1] or col_flag[col][i - 1]:
                        continue
                    else:
                        block_flag[row // 3][col // 3][i - 1] = row_flag[row][i - 1] = col_flag[col][i - 1] = True
                        board[row][col] = str(i)
                        if backtrack(row, col + 1):
                            return True
                        block_flag[row // 3][col // 3][i - 1] = row_flag[row][i - 1] = col_flag[col][i - 1] = False
                        board[row][col] = "."

        backtrack(0, 0)
        # print(board)


if __name__ == "__main__":
    S = Solution()
    S.solveSudoku(
        board=[["5", "3", ".", ".", "7", ".", ".", ".", "."],
               ["6", ".", ".", "1", "9", "5", ".", ".", "."],
               [".", "9", "8", ".", ".", ".", ".", "6", "."],
               ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
               ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
               ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
               [".", "6", ".", ".", ".", ".", "2", "8", "."],
               [".", ".", ".", "4", "1", "9", ".", ".", "5"],
               [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    )
