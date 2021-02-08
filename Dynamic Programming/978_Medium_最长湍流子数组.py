from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        # dp[i]表示以第i个数字结尾的最长湍流字串的长度
        if len(arr) == 1:
            return 1
        dp = [1] * len(arr)
        dp[0] = 1
        dp[1] = 2 if arr[0] != arr[1] else 1
        for i in range(2, len(arr)):
            if arr[i] == arr[i - 1]:
                dp[i] = 1
            else:
                if (arr[i] - arr[i - 1]) * (arr[i - 1] - arr[i - 2]) < 0:
                    dp[i] = dp[i - 1] + 1
                else:
                    dp[i] = 2
        return max(dp)


if __name__ == "__main__":
    S = Solution()
    print(S.maxTurbulenceSize([9, 4, 2, 10, 7, 8, 8, 1, 9]))
    print(S.maxTurbulenceSize([4, 8, 12, 16]))
