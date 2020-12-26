from typing import List
from itertools import product
import math


class Solution:
    def multinomial(self, n):
        return math.factorial(sum(n)) / math.prod([math.factorial(i) for i in n])

    def getProbability(self, balls):
        print(self.multinomial([1, 2, 3]))
        k, n, Q = len(balls), sum(balls) // 2, 0
        arrays = [range(0, i + 1) for i in balls]
        t = list(product(*arrays))
        for i in range(len(t)):
            if sum(t[i]) == n and t[i].count(0) == t[-i - 1].count(0):
                Q += self.multinomial(t[i]) * self.multinomial(t[-i - 1])

        return Q / self.multinomial(list(balls))


if __name__ == "__main__":
    S = Solution()
    print(S.getProbability(balls=[6, 6, 6, 6, 6, 6]))
