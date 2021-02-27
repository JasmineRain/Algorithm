from typing import List
from collections import Counter


class Solution:

    # 单次遍历
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_flag = [{} for _ in range(9)]
        col_flag = [{} for _ in range(9)]
        block_flag = [{} for _ in range(9)]
        for i in range(len(board)):
            for j in range(len(board[i])):
                num = board[i][j]
                if num != ".":
                    num = int(num)
                    idx = (i // 3) * 3 + j // 3
                    row_flag[i][num] = row_flag[i].get(num, 0) + 1
                    col_flag[j][num] = col_flag[j].get(num, 0) + 1
                    block_flag[idx][num] = block_flag[idx].get(num, 0) + 1

                    if row_flag[i][num] > 1 or col_flag[j][num] > 1 or block_flag[idx][num] > 1:
                        return False
        return True



    # 暴力遍历三次
    # def isValidSudoku(self, board: List[List[str]]) -> bool:
    #     if self.checkRow(board) and self.checkCol(board) and self.checkBlock(board):
    #         return True
    #     return False
    #
    # def checkRow(self, board):
    #     for i in range(len(board)):
    #         exist = Counter()
    #         for j in range(len(board[i])):
    #             if board[i][j] in exist:
    #                 return False
    #             elif board[i][j] != ".":
    #                 exist[board[i][j]] = 1
    #     return True
    #
    # def checkCol(self, board):
    #     for i in range(len(board)):
    #         exist = Counter()
    #         for j in range(len(board[i])):
    #             if board[j][i] in exist:
    #                 return False
    #             elif board[j][i] != ".":
    #                 exist[board[j][i]] = 1
    #     return True
    #
    # def checkBlock(self, board):
    #     for i in range(3):
    #         for j in range(3):
    #             exist = Counter()
    #             for r in range(i * 3, (i + 1) * 3):
    #                 for c in range(j * 3, (j + 1) * 3):
    #                     if board[r][c] in exist:
    #                         return False
    #                     elif board[r][c] != ".":
    #                         exist[board[r][c]] = 1
    #     return True


if __name__ == "__main__":
    S = Solution()
    print(S.isValidSudoku([
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]))
    print(S.isValidSudoku([
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]))
