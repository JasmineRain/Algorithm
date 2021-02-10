class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        chars = ['a', 'b', 'c']
        ans = []

        def backtrack(trace):
            if len(trace) == n:
                ans.append(trace + "")
                return

            for c in chars:
                if len(trace) >= 1 and c == trace[-1]:
                    continue
                else:
                    backtrack(trace + c)

        backtrack("")
        print(ans)
        return ans[k - 1] if k <= len(ans) else ""


if __name__ == "__main__":
    S = Solution()
    print(S.getHappyString(n=2, k=4))
