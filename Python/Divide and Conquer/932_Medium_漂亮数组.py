from typing import List


class Solution:
    def beautifulArray(self, N: int) -> List[int]:

        memo = {
            1: [1]
        }

        def divide_conquer(limit):
            if limit not in memo:
                odds = divide_conquer((limit + 1) // 2)
                evens = divide_conquer(limit//2)
                memo[limit] = [odd * 2 - 1 for odd in odds] + [even * 2 for even in evens]
            return memo[limit]

        return divide_conquer(N)


if __name__ == "__main__":
    S = Solution()
    print(S.beautifulArray(4))
    print(S.beautifulArray(5))
