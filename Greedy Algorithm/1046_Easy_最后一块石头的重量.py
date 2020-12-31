from typing import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        minus = [-stones[i] for i in range(len(stones))]
        heapq.heapify(minus)
        while len(minus) >= 2:
            s1 = - heapq.heappop(minus)
            s2 = - heapq.heappop(minus)
            if s1 - s2:
                heapq.heappush(minus, - (s1 - s2))

        return - minus[0] if minus else 0


if __name__ == "__main__":
    S = Solution()
    print(S.lastStoneWeight([2, 7, 4, 1, 8, 1]))
