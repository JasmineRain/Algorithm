class Solution:
    def numDecodings(self, s: str) -> int:

        if len(s) == 0:
            return 0

        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 0 if s[0] == "0" else 1

        for i in range(2, len(s) + 1):
            if s[i-1] == "0":
                if s[i-2] not in ['1', '2']:
                    return 0
                else:
                    dp[i] = dp[i-2]
            else:

                if s[i-2] == "1" or (s[i-2] == "2" and 1 <= int(s[i-1]) <= 6):
                    dp[i] = dp[i-1] + dp[i-2]
                else:
                    dp[i] = dp[i-1]

        print(dp)
        return dp[len(s)]

    def numDecodings2(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        if s[0] == '0':
            dp[1] = 0
        else:
            dp[1] = 1
        for i in range(2, len(s) + 1):
            if s[i - 1] != '0' and 1 <= int(s[i - 2] + s[i - 1]) <= 26:
                # 当前位和前一位都不为'0'
                if s[i - 2] != '0':
                    dp[i] = dp[i - 1] + dp[i - 2]
                # 当前位不为'0',前一位为'0'
                if s[i - 2] == '0':
                    dp[i] = dp[i - 1]
            else:
                if s[i - 1] == '0':
                    # 当前位为'0',且和前一位拼合后合法，'0'不能单独拎出来
                    if int(s[i - 2] + s[i - 1]) >= 1 and int(s[i - 2] + s[i - 1]) <= 26:
                        dp[i] = dp[i - 2]
                    # 当前位为'0',且和前一位拼合后不合法
                    else:
                        dp[i] = 0
                elif int(s[i - 2] + s[i - 1]) > 26:
                    dp[i] = dp[i - 1]
        print(dp)
        return dp[len(s)]


# s[i-1] in ['1', '2', '3', '4', '5', '6'] and s[i-2] in ['1', '2']
if __name__ == "__main__":
    S = Solution()
    print(S.numDecodings(s="01"))
    print(S.numDecodings2(s="01"))
