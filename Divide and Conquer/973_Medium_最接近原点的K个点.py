from typing import List
import random
import heapq


class Solution:

    # lambda表达式直接排序
    # def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
    #     points.sort(key= lambda x: x[0] ** 2 + x[1] ** 2)
    #     return points[:K]

    # 最小堆
    # def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
    #     ans = []
    #
    #     for i in range(len(points)):
    #         if i + 1 <= K:
    #             heapq.heappush(ans, [-points[i][0]**2 - points[i][1]**2, points[i]])
    #         else:
    #             heapq.heappushpop(ans, [-points[i][0]**2 - points[i][1]**2, points[i]])
    #
    #     return [ans[i][1] for i in range(len(ans))]

    # 快排
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:

        left, right = 0, len(points) - 1

        def partition(s, e):
            # 默认取开始元素为轴
            # axis = points[s][0] ** 2 + points[s][1] ** 2

            # 随机化取轴
            idx = random.randint(s, e)
            points[s], points[idx] = points[idx], points[s]
            axis = points[s][0] ** 2 + points[s][1] ** 2
            while s != e:
                while s < e and points[e][0] ** 2 + points[e][1] ** 2 >= axis:
                    e -= 1
                points[s], points[e] = points[e], points[s]
                while s < e and points[s][0] ** 2 + points[s][1] ** 2 <= axis:
                    s += 1
                points[s], points[e] = points[e], points[s]

            return s

        while True:
            res = partition(left, right)
            if res == K - 1:
                return points[:K]
            elif res < K - 1:
                left = res + 1
            else:
                right = res - 1


if __name__ == "__main__":
    S = Solution()
    print(S.kClosest(points=[[0, 1], [1, 0]], K=2))
    print(S.kClosest(points=[[1, 3], [-2, 2]], K=1))
    print(S.kClosest(points=[[3, 3], [5, -1], [-2, 4]], K=2))
    print(S.kClosest(
        points=[[68, 97], [34, -84], [60, 100], [2, 31], [-27, -38], [-73, -74], [-55, -39], [62, 91], [62, 92],
                [-57, -67]], K=5))
