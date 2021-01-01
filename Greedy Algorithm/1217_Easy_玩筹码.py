from typing import List


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:

        odd = even = 0

        for item in position:
            if item % 2 == 0:
                even += 1
            else:
                odd += 1

        return min(odd, even)


if __name__ == "__main__":
    S = Solution()
    print(S.minCostToMoveChips(position=[1, 2, 3]))
    print(S.minCostToMoveChips(position=[2, 2, 2, 3, 3]))
