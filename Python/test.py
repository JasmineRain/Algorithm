class Solution:

    def divide(self, s):

        ans = []

        # backtrack     start
        def backtrack(temp, start):
            if start == len(s):
                ans.append(len(temp))
            for i in range(start, len(s)):
                subs = s[start: i + 1]
                if self.check(subs):
                    backtrack(temp + [subs], i + 1)

        backtrack([], 0)

        return min(ans) - 1

    # check available string
    def check(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True


if __name__ == "__main__":
    S = Solution()
    # expect output 1
    print(S.divide("aab"))
    print(S.divide("aaaaa"))
