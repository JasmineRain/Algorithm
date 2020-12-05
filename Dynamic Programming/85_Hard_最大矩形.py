from typing import List


class Solution:
    # 半暴力DP
    # def maximalRectangle(self, matrix: List[List[str]]) -> int:
    #
    #     if not matrix:
    #         return 0
    #
    #     nrow = len(matrix)
    #     ncol = len(matrix[0])
    #     max_area = 0
    #     dp = [[0 for c in range(ncol)] for r in range(nrow)]
    #
    #     for i in range(0, nrow):
    #         for j in range(0, ncol):
    #
    #             if matrix[i][j] == "0":
    #                 dp[i][j] = 0
    #                 continue
    #
    #             # 先计算最大宽度
    #             width = dp[i][j] = dp[i][j - 1] + 1 if j else 1
    #
    #             # 遍历所有可能长度计算面积
    #             for k in range(i, -1, -1):
    #                 height = i - k + 1
    #                 width = min(width, dp[k][j])
    #                 area = width * height
    #                 if area > max_area:
    #                     max_area = area
    #     return max_area

    # 优化式DP
    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        if not matrix:
            return 0

        nrow = len(matrix)
        ncol = len(matrix[0])

        left = [0] * ncol
        right = [ncol] * ncol
        height = [0] * ncol
        max_area = 0

        for i in range(0, nrow):

            for j in range(0, ncol):
                height[j] = height[j] + 1 if matrix[i][j] == "1" else 0

            max_left = 0
            for j in range(0, ncol):
                if matrix[i][j] == "1":
                    left[j] = max(max_left, left[j])
                else:
                    max_left = j + 1
                    left[j] = 0

            min_right = ncol
            for j in range(ncol-1, -1, -1):
                if matrix[i][j] == "1":
                    right[j] = min(min_right, right[j])
                else:
                    min_right = j
                    right[j] = ncol

            for k in range(0, ncol):
                max_area = max(max_area, height[k] * (right[k] - left[k]))

            # print("***")
            # print(left)
            # print(height)
            # print(right)
            # print("***")

        return max_area


if __name__ == "__main__":
    S = Solution()
    print(S.maximalRectangle(matrix=[["1"]]))
