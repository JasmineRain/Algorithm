from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        ans = 0
        flag = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not grid[i][j]:
                    flag[i][j] = True

        def getMovable(row, col):
            return [
                row - 1 >= 0 and not flag[row - 1][col],
                col + 1 < len(grid[0]) and not flag[row][col + 1],
                row + 1 < len(grid) and not flag[row + 1][col],
                col - 1 >= 0 and not flag[row][col - 1]
            ]

        def backtrack(row, col, trace):
            info = getMovable(row, col)
            if sum(info) == 0:
                nonlocal ans
                ans = max(ans, sum(trace + [grid[row][col]]))
                return

            flag[row][col] = True
            trace.append(grid[row][col])
            if info[0]:
                backtrack(row - 1, col, trace)
            if info[1]:
                backtrack(row, col + 1, trace)
            if info[2]:
                backtrack(row + 1, col, trace)
            if info[3]:
                backtrack(row, col - 1, trace)
            flag[row][col] = False
            trace.pop()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    backtrack(i, j, [])

        return ans


if __name__ == "__main__":
    S = Solution()
    print(S.getMaximumGold(grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]))
