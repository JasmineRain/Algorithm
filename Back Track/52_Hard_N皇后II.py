class Solution:
    def totalNQueens(self, n: int) -> int:

        board = [[False for _ in range(n)] for _ in range(n)]

        def backtrack(board, row):
            if row == n:
                return 1
            count = 0
            for col in range(n):
                if is_valid(board, row, col):
                    board[row][col] = True
                    row += 1
                    count += backtrack(board, row)
                    row -= 1
                    board[row][col] = False
            return count

        def is_valid(board, row, col):
            for r in range(row):
                if board[r][col]:
                    return False
            for k in range(1, min(row, col) + 1):
                if board[row - k][col - k]:
                    return False
            for k in range(1, min(row, n - 1 - col) + 1):
                if board[row - k][col + k]:
                    return False
            return True

        return backtrack(board, 0)


if __name__ == "__main__":
    S = Solution()
    print(S.totalNQueens(n=8))
