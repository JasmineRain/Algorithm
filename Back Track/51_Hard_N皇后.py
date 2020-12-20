from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []

        def backtrack(board, row):
            if row == n:
                ans.append(board.copy())
                return

            for c in range(0, n):
                init = "." * n
                if is_valid(board, row, c):
                    init = list(init)
                    init[c] = "Q"
                    board.append("".join(init))
                    backtrack(board, row + 1)
                    board.pop()

        def is_valid(board, row, col):
            for r in range(row):
                if board[r][col] == "Q":
                    return False
            for k in range(1, min(row, col) + 1):
                if board[row - k][col - k] == "Q":
                    return False
            for k in range(1, min(row, n - 1 - col) + 1):
                if board[row - k][col + k] == "Q":
                    return False
            return True
        backtrack([], 0)
        return ans


if __name__ == "__main__":
    S = Solution()
    print(S.solveNQueens(n=4))
