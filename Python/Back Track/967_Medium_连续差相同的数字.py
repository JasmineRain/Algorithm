from typing import List


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:

        ans = []

        def backtrack(trace):

            if len(trace) == n:
                ans.append(int(trace))
                return
            for i in range(0, 10):
                if abs(i - int(trace[-1])) != k:
                    continue
                else:
                    backtrack(trace + str(i))

        for i in range(1, 10):
            backtrack(str(i))

        return ans


if __name__ == "__main__":
    S = Solution()
    print(S.numsSameConsecDiff(n=2, k=1))
