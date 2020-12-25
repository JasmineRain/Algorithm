from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(value, track):
            if len(track) == 2 * n:
                if value == 0:
                    ans.append(track)
                    return
                else:
                    return
            if value + 1 <= n:
                backtrack(value + 1, track + "(")
            if value - 1 >= 0:
                backtrack(value - 1, track + ")")

        backtrack(0, "")
        return ans


if __name__ == "__main__":
    S = Solution()
    print(S.generateParenthesis(n=3))
