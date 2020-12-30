from typing import List
from collections import deque


class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        minus = deque()
        A.sort()
        for i in range(len(A)):
            if A[i] < 0:
                minus.append(i)
        while K > 0 and minus:
            idx = minus.popleft()
            A[idx] = -A[idx]
            K -= 1

        if K == 0 or K % 2 == 0:
            return sum(A)
        else:
            return sum(A) - 2 * min(A)




if __name__ == "__main__":
    S = Solution()
    print(S.largestSumAfterKNegations(A=[4, 2, 3], K=1))
    print(S.largestSumAfterKNegations(A=[3, -1, 0, 2], K=3))
    print(S.largestSumAfterKNegations(A=[2, -3, -1, 5, -4], K=2))
