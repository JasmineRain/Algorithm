class Solution:
    def numberOfMatches(self, n: int) -> int:
        total = 0
        while n != 1:
            flag = n % 2
            n = n // 2
            total += n
            n += flag

        return total


if __name__ == "__main__":
    S = Solution()
    print(S.numberOfMatches(n=14))
