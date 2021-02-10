from typing import List


class Solution:
    def permutation(self, S: str) -> List[str]:
        ans = []
        flag = [False] * len(S)

        def backtrack(trace):
            if len(trace) == len(S):
                ans.append(trace)
            for i in range(0, len(S)):
                if flag[i]:
                    continue
                else:
                    flag[i] = True
                    backtrack(trace + S[i])
                    flag[i] = False

        backtrack("")
        return ans


if __name__ == "__main__":
    S = Solution()
    print(S.permutation(S="qwe"))
