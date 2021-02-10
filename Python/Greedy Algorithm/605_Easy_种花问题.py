from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        if len(flowerbed) == 1:
            return flowerbed[0] == 0 or n == 0

        count = 0
        for i in range(len(flowerbed)):

            if count >= n:
                break

            if i == 0:
                if not flowerbed[i] and not flowerbed[i + 1]:
                    flowerbed[i] = 1
                    count += 1
            elif i == len(flowerbed) - 1:
                if not flowerbed[i] and not flowerbed[i - 1]:
                    flowerbed[i] = 1
                    count += 1
            else:
                if not flowerbed[i] and not flowerbed[i - 1] and not flowerbed[i + 1]:
                    flowerbed[i] = 1
                    count += 1

        return count >= n


if __name__ == "__main__":
    S = Solution()
    print(S.canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=1))
    print(S.canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=2))
