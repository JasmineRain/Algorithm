from typing import List
from heapq import nlargest


class Solution:
    def findMaximizedCapital(self, k: int, W: int, Profits: List[int], Capital: List[int]) -> int:

        if W >= max(Capital):
            return W + sum(nlargest(k, Profits))

        for i in range(min(k, len(Profits))):
            idx = -1
            cur = 0
            for j in range(len(Profits)):
                if W < Capital[j]:
                    continue
                else:
                    if Profits[j] > cur:
                        idx = j
                        cur = Profits[j]

            if idx == -1:
                break

            W += Profits[idx]
            Capital[idx] = float("inf")

        return W


if __name__ == "__main__":
    S = Solution()
    print(S.findMaximizedCapital(k=2, W=0, Profits=[1, 2, 3], Capital=[0, 1, 1]))
