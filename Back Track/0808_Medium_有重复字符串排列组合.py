from typing import List


class Solution:
    def permutation(self, S: str) -> List[str]:
        ans = []
        S = sorted(S)
        flag = [False] * len(S)

        def backtrack(trace):
            if len(trace) == len(S):
                ans.append(trace)
                return
            for i in range(len(S)):
                if flag[i]:
                    continue
                if i > 0 and S[i] == S[i-1] and not flag[i-1]:
                    continue
                else:
                    flag[i] = True
                    backtrack(trace + S[i])
                    flag[i] = False

        backtrack("")
        return ans


if __name__ == "__main__":
    S = Solution()
    print(S.permutation(S="qqe"))
