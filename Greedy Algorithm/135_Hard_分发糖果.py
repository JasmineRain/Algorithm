from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:

        left = [1] * len(ratings)
        right = [1] * len(ratings)
        ans = 0

        # right forward
        # fix the ans in right
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                right[i] = right[i - 1] + 1

        ans = right[-1]
        # left forward
        # fix the ans in left
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                left[i] = left[i + 1] + 1
            ans += max(left[i], right[i])

        return ans


if __name__ == "__main__":
    S = Solution()
    print(S.candy([1, 0, 2]))
    print(S.candy([1, 2, 2]))
    print(S.candy([1, 2, 87, 87, 87, 2, 1]))
