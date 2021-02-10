class Solution:
    def balancedStringSplit(self, s: str) -> int:
        left = right = 0
        ans = 0

        for i in range(len(s)):
            if s[i] == "L":
                left += 1
            else:
                right += 1

            if left == right:
                ans += 1

        return ans


if __name__ == "__main__":
    S = Solution()
    print(S.balancedStringSplit(s="RLRRLLRLRL"))
    print(S.balancedStringSplit(s="RLLLLRRRLR"))
    print(S.balancedStringSplit(s="LLLLRRRR"))
