from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x: x[1])
        count = 0
        end = - float("inf")

        for i in range(len(points)):
            if points[i][0] > end:
                count += 1
                end = points[i][1]

        return count


if __name__ == "__main__":
    S = Solution()
    print(S.findMinArrowShots(points=[[10, 16], [2, 8], [1, 6], [7, 12]]))
    print(S.findMinArrowShots(points=[[1, 2], [3, 4], [5, 6], [7, 8]]))
    print(S.findMinArrowShots(points=[[1, 2], [2, 3], [3, 4], [4, 5]]))
    print(S.findMinArrowShots(points=[[2, 3], [2, 3]]))
