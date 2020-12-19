from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        # 定义dp[i]为s的前i个字符能否拆分成功
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(0, i):
                if dp[j] and s[j: i] in wordDict:
                    dp[i] = True
        print(dp[1:])
        return dp[-1]

    def wordBreak2(self, s: str, wordDict: List[str]) -> bool:

        # 定义dp[i]为s的前i个字符能否拆分成功
        dp = [False] * len(s)
        for i in range(0, len(s)):
            dp[i] = s[:i + 1] in wordDict
            for j in range(0, i):
                if dp[j] and s[j + 1: i + 1] in wordDict:
                    dp[i] = True
                    break
        # print(dp)
        return dp[-1]


if __name__ == "__main__":
    S = Solution()
    print(S.wordBreak(s="applepenapple", wordDict=["apple", "pen"]))
    print(S.wordBreak2(s="applepenapple", wordDict=["apple", "pen"]))
