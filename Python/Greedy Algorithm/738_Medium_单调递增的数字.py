class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:

        if N // 10 == 0:
            return N

        s = str(N)
        idx = 0
        ans = [s[0]]

        for i in range(1, len(s)):
            if s[i] > s[i - 1]:
                ans.append(s[i])
                idx = i
            elif s[i] == s[i - 1]:
                ans.append(s[i])
                continue
            else:
                if i - 1 == idx:
                    last = ans.pop()
                    ans.append(str(int(last) - 1))
                    ans += ['9'] * (len(s) - i)
                    break
                else:
                    ans = ans[:idx] + [str(int(s[idx]) - 1)] + ['9'] * (len(s) - idx - 1)
                    break

        return int("".join(ans))


if __name__ == "__main__":
    S = Solution()
    print(S.monotoneIncreasingDigits(10))
    print(S.monotoneIncreasingDigits(1234))
    print(S.monotoneIncreasingDigits(332))
