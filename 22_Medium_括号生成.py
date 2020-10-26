from typing import List


# 回溯法，考虑的问题是如何加入括号并且可以保证合法
# track中，左括号数目不超过括号对数目，右括号数不超过左括号数
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        track = []
        ans = []

        def backtrack(left, right):
            if len(track) == 2 * n:
                ans.append("".join(track))
            else:
                if left < n:
                    track.append('(')
                    backtrack(left + 1, right)
                    track.pop()
                if right < left:
                    track.append(')')
                    backtrack(left, right + 1)
                    track.pop()

        backtrack(0, 0)
        return ans


if __name__ == "__main__":
    S = Solution()
    print(S.generateParenthesis(n=4))
