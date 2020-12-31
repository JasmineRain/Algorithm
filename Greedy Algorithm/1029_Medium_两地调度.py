from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # 假设全部去A市，根据A、B路费差排序后选出应该去B的N个人
        total = 0
        for i in range(len(costs)):
            total += costs[i][0]

        costs.sort(key=lambda x: x[0] - x[1], reverse=True)

        for i in range(len(costs) // 2):
            total += costs[i][1] - costs[i][0]

        return total


if __name__ == "__main__":
    S = Solution()
    print(S.twoCitySchedCost([[10, 20],
                              [30, 200],
                              [400, 50],
                              [30, 20]]))
