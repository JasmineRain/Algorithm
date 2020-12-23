from typing import List
import math


class Solution:
    def numSquarefulPerms(self, A: List[int]) -> int:
        ans = []
        flag = [False] * len(A)
        A.sort()

        def backtrack(trace):
            if len(trace) == len(A):
                ans.append(trace.copy())
                return
            for i in range(len(A)):
                if flag[i]:
                    continue
                if len(trace) >= 1:
                    addition = A[i] + trace[-1]
                    if addition != int(math.sqrt(addition)) ** 2:
                        continue
                if i > 0 and A[i] == A[i - 1] and not flag[i - 1]:
                    continue
                flag[i] = True
                trace.append(A[i])
                backtrack(trace)
                flag[i] = False
                trace.pop()

        backtrack([])
        # print(ans)
        return len(ans)


if __name__ == "__main__":
    S = Solution()
    print(S.numSquarefulPerms([65, 44, 5, 11]))
