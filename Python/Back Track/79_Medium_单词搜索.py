from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        flag = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

        def backtrack(index, row, col):

            if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or flag[row][col] or board[row][col] != word[index]:
                return False

            if index == len(word) - 1 and board[row][col] == word[-1]:
                return True

            flag[row][col] = True
            if backtrack(index + 1, row - 1, col):
                return True
            if backtrack(index + 1, row + 1, col):
                return True
            if backtrack(index + 1, row, col - 1):
                return True
            if backtrack(index + 1, row, col + 1):
                return True
            flag[row][col] = False
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if backtrack(0, i, j):
                        return True
        return False

if __name__ == "__main__":
    S = Solution()
    print(
        S.exist(board=[
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
        ], word="SEE"))
