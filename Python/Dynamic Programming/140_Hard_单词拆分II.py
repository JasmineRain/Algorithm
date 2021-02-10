from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        dp = [False] * len(s)
        for i in range(0, len(s)):
            dp[i] = s[:i + 1] in wordDict
            for j in range(0, i):
                if dp[j] and s[j + 1: i + 1] in wordDict:
                    dp[i] = True
                    break

        # 注意dp定义的是前i个元素，因此选取子串从后开始选取，否则需要重新计算dp
        # 从后选取子串后，最后拼接前需要倒序
        def summarize(end, temp):
            if end == -1:
                datas.append(temp)
                return
            for i in range(end, -2, -1):
                if dp[i] and s[i + 1: end + 1] in wordDict:
                    summarize(i, temp + [s[i + 1: end + 1]])

        datas = []
        ans = []
        summarize(len(s) - 1, [])
        # print(datas)
        for data in datas:
            data.reverse()
            ans.append(" ".join(data))

        return ans


if __name__ == "__main__":
    S = Solution()
    print(S.wordBreak(s="pineapplepenapple", wordDict=["apple", "pen", "applepen", "pine", "pineapple"]))
