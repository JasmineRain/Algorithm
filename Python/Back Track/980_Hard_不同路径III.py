from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        ans = []
        srow, scol = 0, 0
        erow, ecol = 0, 0
        length = 0
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    srow, scol = i, j
                    length += 1
                elif grid[i][j] == 2:
                    erow, ecol = i, j
                    length += 1
                elif grid[i][j] == -1:
                    visited[i][j] = True
                else:
                    length += 1

        def backtrack(row, col, trace):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or visited[row][col]:
                return
            if row == erow and col == ecol:
                if len(trace) == length - 1:
                    ans.append(trace + [(row, col)])
                else:
                    return
            visited[row][col] = True
            trace.append((row, col))
            backtrack(row + 1, col, trace)
            backtrack(row - 1, col, trace)
            backtrack(row, col + 1, trace)
            backtrack(row, col - 1, trace)
            trace.pop()
            visited[row][col] = False

        backtrack(srow, scol, [])
        # for i in range(len(ans)):
        #     print(ans[i])
        return len(ans)


if __name__ == "__main__":
    S = Solution()
    print(S.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,0,2]]))
