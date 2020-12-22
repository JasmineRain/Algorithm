from typing import List


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        ans = []

        def backtrack(index, trace):
            if index == len(S):
                ans.append(trace)
                return
            if not S[index].isalpha():
                backtrack(index + 1, trace + S[index])
            else:
                backtrack(index + 1, trace + S[index])
                backtrack(index + 1, trace + S[index].upper() if S[index].islower() else trace + S[index].lower())

        backtrack(0, "")
        return ans


if __name__ == "__main__":
    S = Solution()
    print(S.letterCasePermutation(S="TB"))
