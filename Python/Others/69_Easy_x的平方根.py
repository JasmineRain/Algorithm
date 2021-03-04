class Solution:
    # def mySqrt(self, x: int) -> int:
    #     left, right = 0, x
    #     ans = -1
    #     while left <= right:
    #         mid = (left + right) // 2
    #         temp = mid * mid
    #         if temp <= x:
    #             ans = mid
    #             left += 1
    #         else:
    #             right = mid - 1
    #     return ans

    def mySqrt(self, x):
        cur = 1
        while True:
            pre = cur
            cur = (cur + x / cur) / 2
            if abs(cur - pre) < 1e-6:
                return int(cur)


if __name__ == "__main__":
    S = Solution()
    print(S.mySqrt(8))
