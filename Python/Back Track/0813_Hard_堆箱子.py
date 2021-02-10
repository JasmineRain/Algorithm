from typing import List


class Solution:
    def pileBox(self, box: List[List[int]]) -> int:
        box = sorted(box, key=lambda x: [x[0], x[1], x[2]], reverse=True)
        # 定义dp[i]为以第i个箱子为顶  能达到的最大高度
        dp = [0] * len(box)

        for i in range(len(box)):
            dp[i] = box[i][2]

            for j in range(0, i):
                if box[i][0] < box[j][0] and box[i][1] < box[j][1] and box[i][2] < box[j][2]:
                    dp[i] = max(dp[i], dp[j] + box[i][2])

        return max(dp)

    # def pileBox(self, box: List[List[int]]) -> int:
    #     box = sorted(box, key=lambda x: [x[0], x[1], x[2]], reverse=True)
    #     flag = [False] * len(box)
    #     ans = 0
    #
    #     def backtrack(w, h, index, last, total):
    #
    #         nonlocal ans
    #         ans = max(ans, total)
    #
    #         for i in range(index, len(box)):
    #             if flag[i] or box[i][0] >= w or box[i][1] >= h or box[i][2] >= last:
    #                 continue
    #             else:
    #                 flag[i] = True
    #                 backtrack(box[i][0], box[i][1], i + 1, box[i][2], total + box[i][2])
    #                 flag[i] = False
    #
    #     backtrack(float("inf"), float("inf"), 0, float("inf"), 0)
    #     return ans


if __name__ == "__main__":
    S = Solution()
    print(S.pileBox(box=[[1, 1, 1], [2, 3, 4], [2, 6, 7], [3, 4, 5]]))
