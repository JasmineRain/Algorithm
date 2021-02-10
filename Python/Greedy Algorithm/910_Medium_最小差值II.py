from typing import List


class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:

        if len(A) == 1:
            return 0

        A.sort()
        ans = A[-1] - A[0]
        for i in range(len(A) - 1):
            maximal = max(A[i] + K, A[-1] - K)
            minimal = min(A[0] + K, A[i + 1] - K)
            ans = min(ans, maximal - minimal)
        return ans


if __name__ == "__main__":
    S = Solution()
    print(S.smallestRangeII(A=[1], K=0))
    print(S.smallestRangeII(A=[0, 10], K=2))
    print(S.smallestRangeII(A=[1, 3, 6], K=3))
