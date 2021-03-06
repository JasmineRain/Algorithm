from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:

        # first calculate all situations utilizing DP
        # 定义dp[i][j]为第i个字符到第j个字符构成的子串是否为回文串
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        ans = []
        for j in range(0, len(s)):
            for i in range(0, j + 1):
                if i == j:
                    dp[i][j] = True
                elif j - i == 1:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]

        def track(i, tmp):
            if i == len(s):
                ans.append(tmp)
            for j in range(i, len(s)):
                if dp[i][j]:
                    track(j + 1, tmp + [s[i: j + 1]])
        track(0, [])
        return ans

    # def partition(self, s: str) -> List[List[str]]:
    #     if s == "":
    #         return []
    #     ans = [[s[0]]]
    #     for i in range(1, len(s)):
    #         curr = s[i]
    #         newAns = []
    #         for item in ans:
    #             newAns.append(item + [curr])
    #             if item[-1] == curr:
    #                 newAns.append(item[0:-1] + [item[-1] + curr])
    #             if len(item) >= 2 and item[-2] == curr:
    #                 newAns.append(item[0:-2] + [item[-2] + item[-1] + curr])
    #         ans = newAns
    #     return ans


if __name__ == "__main__":
    S = Solution()
    print(S.partition(s="aab"))
