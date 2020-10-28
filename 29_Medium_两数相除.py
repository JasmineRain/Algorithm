class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        if abs(divisor) > abs(dividend):
            return 0
        sign = (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0)
        ans = 0
        dividend = abs(dividend)
        divisor = abs(divisor)
        while divisor <= dividend:
            quotient = 1
            value = divisor

            while value + value <= dividend:
                value += value
                quotient += quotient
            ans += quotient
            dividend -= value

        ans = ans if sign else -ans

        if (ans > 2**31 - 1) or (ans < -2**31):
            return 2**31 - 1
        else:
            return ans


if __name__ == "__main__":
    S = Solution()
    print(2**31)
    print(S.divide(dividend=-1, divisor=1))