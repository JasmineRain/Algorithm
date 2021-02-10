from typing import List
from collections import deque
import heapq


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        exist = 0
        info = []
        trips.sort(key=lambda x: x[1])

        for i in range(len(trips)):

            while info and info[0][0] <= trips[i][1]:
                _, drop = heapq.heappop(info)
                exist -= drop

            if exist + trips[i][0] <= capacity:
                exist += trips[i][0]
                heapq.heappush(info, [trips[i][2], trips[i][0]])
            else:
                return False

        return True


if __name__ == "__main__":
    S = Solution()
    print(S.carPooling(trips=[[9, 3, 4], [9, 1, 7], [4, 2, 4], [7, 4, 5]], capacity=23))
    print(S.carPooling(trips=[[3, 2, 8], [4, 4, 6], [10, 8, 9]], capacity=11))
    print(S.carPooling(trips=[[2, 1, 5], [3, 3, 7]], capacity=4))
    print(S.carPooling(trips=[[2, 1, 5], [3, 3, 7]], capacity=5))
    print(S.carPooling(trips=[[2, 1, 5], [3, 5, 7]], capacity=3))
    print(S.carPooling(trips=[[3, 2, 7], [3, 7, 9], [8, 3, 9]], capacity=11))
