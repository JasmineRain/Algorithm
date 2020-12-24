from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:
        ans = []
        s = sorted(s)
        flag = [False] * len(s)

        def backtrack(trace):
            if len(trace) == len(s):
                ans.append(trace)
                return
            for i in range(len(s)):
                if flag[i]:
                    continue
                if i > 0 and s[i] == s[i-1] and not flag[i-1]:
                    continue
                else:
                    flag[i] = True
                    backtrack(trace + s[i])
                    flag[i] = False

        backtrack("")
        return ans


if __name__ == "__main__":
    S = Solution()
    print(S.permutation(s="aab"))
