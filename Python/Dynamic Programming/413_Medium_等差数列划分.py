from typing import List


class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        # 定义dp[i]为以第i个数字结尾的等差子数组个数
        dp = [0] * len(A)
        for i in range(2, len(A)):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                dp[i] = dp[i - 1] + 1
        # print(dp)
        return sum(dp)


if __name__ == "__main__":
    S = Solution()
    print(S.numberOfArithmeticSlices(A=[1, 1, 1, 2, 3, 4, 5]))
