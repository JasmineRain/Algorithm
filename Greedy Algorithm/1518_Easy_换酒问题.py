class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        remain = numBottles
        ans = numBottles

        while remain >= numExchange:
            ans += remain // numExchange
            remain = remain // numExchange + remain % numExchange

        return ans


if __name__ == "__main__":
    S = Solution()
    print(S.numWaterBottles(numBottles=9, numExchange=3))
    print(S.numWaterBottles(numBottles=15, numExchange=4))
    print(S.numWaterBottles(numBottles=5, numExchange=5))
    print(S.numWaterBottles(numBottles=2, numExchange=3))
