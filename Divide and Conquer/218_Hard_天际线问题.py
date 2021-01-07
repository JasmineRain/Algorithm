from collections import Counter
from typing import List


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        count = Counter()

        for i in range(len(buildings)):
            if buildings[i][2] not in count:
                count[buildings[i][2]] = [buildings[i][0], buildings[i][1]]
            else:
                count[buildings[i][2]] = []


if __name__ == "__main__":
    S = Solution()
    print(S.getSkyline(buildings=[[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]))
    print(S.getSkyline(buildings=[[0, 2, 3], [2, 5, 3]]))
