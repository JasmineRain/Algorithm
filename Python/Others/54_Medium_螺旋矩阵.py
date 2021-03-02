from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        while left <= right and top <= bottom:
            for col in range(left, right + 1):
                ans.append(matrix[top][col])
            for row in range(top + 1, bottom + 1):
                ans.append(matrix[row][right])
            if left < right and top < bottom:
                for col in range(right - 1, left, -1):
                    ans.append(matrix[bottom][col])
                for row in range(bottom, top, -1):
                    ans.append(matrix[row][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        return ans


if __name__ == "__main__":
    S = Solution()
    print(S.spiralOrder(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(S.spiralOrder(matrix=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
