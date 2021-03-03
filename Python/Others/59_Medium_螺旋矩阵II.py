from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[1 for _ in range(n)] for _ in range(n)]
        left, right, top, bottom = 0, n - 1, 0, n - 1
        value = 1
        while left <= right and top <= bottom:
            for col in range(left, right + 1):
                ans[top][col] = value
                value += 1
            for row in range(top + 1, bottom + 1):
                ans[row][right] = value
                value += 1
            if left < right and top < bottom:
                for col in range(right - 1, left, -1):
                    ans[bottom][col] = value
                    value += 1
                for row in range(bottom, top, -1):
                    ans[row][left] = value
                    value += 1
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1

        return ans


if __name__ == "__main__":
    S = Solution()
    print(S.generateMatrix(3))
