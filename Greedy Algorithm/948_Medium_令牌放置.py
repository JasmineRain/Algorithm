from typing import List
from collections import deque


class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        tokens.sort()
        queue = deque(tokens)
        ans = 0
        bonus = 0

        while queue and (P >= queue[0] or bonus > 0):
            while queue and P >= queue[0]:
                bonus += 1
                P -= queue[0]
                queue.popleft()
            ans = max(ans, bonus)

            if queue and bonus > 0:
                P += queue.pop()
                bonus -= 1

        return ans


if __name__ == "__main__":
    S = Solution()
    print(S.bagOfTokensScore(tokens=[100, 200], P=150))
    print(S.bagOfTokensScore(tokens=[100, 200, 300, 400], P=200))
