class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        if abs(divisor) > abs(dividend):
            return 0
        sign = (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0)
        quotient = 0
        dividend = abs(dividend)
        divisor = abs(divisor)
        value = divisor
        while value <= dividend:
            quotient += 1
            value += divisor

        quotient = quotient if sign else -quotient
        if (quotient > 2**31 - 1) or (quotient < -2**31):
            return 2**31 - 1
        else:
            return quotient


if __name__ == "__main__":
    S = Solution()
    print(2**31)
    print(S.divide(dividend=-1, divisor=1))