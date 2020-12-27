from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        value = 0
        start = 0
        min_value = 0
        for i in range(len(gas)):
            value += gas[i] - cost[i]
            if value <= min_value:
                min_value = value
                start = i

        return (start + 1) % len(gas) if value >= 0 else -1


if __name__ == "__main__":
    S = Solution()
    print(S.canCompleteCircuit(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2]))
    print(S.canCompleteCircuit(gas=[2, 3, 4], cost=[3, 4, 3]))
