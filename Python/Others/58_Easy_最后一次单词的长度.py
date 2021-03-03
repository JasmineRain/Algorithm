class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        return len(s.strip().split(" ")[-1])


if __name__ == "__main__":
    S = Solution()
    print(S.lengthOfLastWord(s="Hello World"))
    print(S.lengthOfLastWord(s=" "))
    print(S.lengthOfLastWord(s="a "))
