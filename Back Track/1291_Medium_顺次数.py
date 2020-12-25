from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = list()
        for i in range(1, 10):
            num = i
            for j in range(i + 1, 10):
                num = num * 10 + j
                if low <= num <= high:
                    ans.append(num)
        return sorted(ans)


if __name__ == "__main__":
    S = Solution()
    print(S.sequentialDigits(low=1000, high=13000))
