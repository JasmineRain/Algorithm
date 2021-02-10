class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        ans = 0

        def backtrack(index, trace):
            if index == len(s):
                nonlocal ans
                ans = max(ans, len(trace))
                return

            for i in range(index, len(s)):
                if s[index: i + 1] in trace:
                    continue
                else:
                    backtrack(i + 1, trace + [s[index: i + 1]])

        backtrack(0, [])
        return ans


if __name__ == "__main__":
    S = Solution()
    print(S.maxUniqueSplit(s="aa"))
